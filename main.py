from RFDSearch import *
from export_browser import *


class RFDScrape:
    """
    The initialization module for gathering RFD data
    and exporting it as HTML doc.
    """

    def __init__(self):
        self.user_input = self._ask_user()
        assert type(self.user_input) == UserInput
        (self.url,
         search_in_titles,
         query) = (generate_url(self.user_input[:-1]),
                   self.user_input[-1],
                   self.user_input[0])

        self.search = RFDSearch(self.url, query, search_in_titles)
        database = self.search.thread_database

        if not rfd_results_empty(database, self.user_input[:-1]):
            ExportToHTML(database)
            print(len(database))

    def _ask_user(self):
        """
        Request the user to specify the query string,
        start date, and end date of search timeline.
        """
        q = input("Enter search query: ")
        print(FOR_USER)

        tf_valid = False
        while not tf_valid:
            tf = input("Indicate how long ago the thread can be posted from "
                       + EXTRA_INFO)
            tf_valid = validate_date(tf)
        tf = standardize_date(tf)

        in_title_valid = False
        while not in_title_valid:
            search_in_titles = input(FOR_USER_2)
            in_title_valid = validate_in_title_option(search_in_titles)
        
        return UserInput(q, tf, search_in_titles)


if __name__ == '__main__':
    r = RFDScrape()
    d = r.search.thread_database
