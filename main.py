from RFDSearch import *
from export_browser import *


class RFDScrape:
    """
    The initialization module for gathering RFD data
    and exporting it as HTML doc.
    """

    def __init__(self):
        self.user_input = self._ask_user()
        self.url = generate_url(self.user_input)

        self.search = RFDSearch(self.url)
        database = self.search.thread_database

        if not rfd_results_empty(database, self.user_input):
            ExportToHTML(database)

    def _ask_user(self):
        """
        Request the user to specify the query string,
        start date, and end date of search timeline.
        """
        q = input("Enter search query: ")
        print(FOR_USER)

        tf_valid = False
        while not tf_valid:
            tf = input("Enter start date " + EXTRA_INFO)
            tf_valid = validate_date(tf)
        tf = standardize_date(tf)

        tt_valid = False
        while not tt_valid:
            tt = input("Enter end date " + EXTRA_INFO)
            tt_valid = validate_date(tt)
        tt = standardize_date(tt)

        return UserInput(q, tf, tt)


if __name__ == '__main__':
    r = RFDScrape()
    d = r.search.thread_database
