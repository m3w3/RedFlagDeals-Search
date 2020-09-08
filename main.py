from RFDSearch import *


class RFDScrape:
    """
    The initialization module for gathering RFD data
    and exporting it as HTML doc.
    """

    def __init__(self):
        # self.user_input, self.sort_by = _ask_user
        self.user_input, self.sort_by = (UserInput('whatthefuck',
                                         '2020-7-20',
                                         '2020-8-18'),
                               None)
        self.url = generate_url(self.user_input)

        self.search = RFDSearch(self.url)
        database = self.search.thread_database

        if not RFD_results_empty(database, self.user_input):
            # TODO: proceed to process database
            pass
        
    def _ask_user(self):
        """
        Request the user to specify the query string,
        start date, and end date of search timeline.
        """
        q = input("Enter search query: ")
        # TODO: convert the part after 'or'
        tf = input("Enter start date " + EXTRA_INFO)
        tt = input("Enter end date " + EXTRA_INFO)
        user_input = UserInput(q, tf, tt) # named tuple, see: constants.py

        # sort by: post date, upvote, score
        sort_by = input("Sort by 'post date', 'upvote', 'score': ")

        return user_input, sort_by

if __name__ == '__main__':
    r = RFDScrape()
##    total_pages = r._total_pages()
##    thread_data = {}
##    curr_page_results = b.find_elements_by_xpath(RESULTS_LIST)
##    t = RFDThread(b, curr_page_results[3])
##    t_info = t._collect_thread_data()
