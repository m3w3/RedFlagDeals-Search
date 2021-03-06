from selenium.webdriver import Chrome
from RFDThread import *
from browser_settings import *
from constants import *


class RFDSearch:
    """
    The initialization module for RedFlagDeals search page using Chrome.
    (the individual search pages' interface)
    """

    def __init__(self, url, query, search_in_titles):
        self.browser = Chrome(options=default_browser_options())
        # self.browser.implicitly_wait(10)
        self.URL = url
        self.page_num = 1
        self.thread_database = {}

        self._go_to_page(self.page_num)
        if not self._no_matches():
            self._aggregate_all_pages(query, search_in_titles)
            self.browser.quit()

    def _no_matches(self):
        """
        Return True if the query returned 0 results. Otherwise False.
        """
        total_count_div = self.browser.find_element_by_xpath(TOTAL_SEARCH_COUNT)
        if total_count_div.text == '0':
            self.browser.quit()
            return True

    def _total_pages(self):
        """
        Return the total number of search pages (i.e. the 'n' in page 1 of n)
        in the current page.
        """
        total_page_div = self.browser.find_element_by_xpath(TOTAL_PAGES)
        return int(total_page_div.text)

    def _go_to_page(self, page_num):
        """
        Go to the search result's given page number, as specified by input.
        """
        self.browser.get(self.URL + str(page_num))
        sleep(0.5)

    def switch_to_main_window(self):
        """
        Switch the browser back to the first tab
        (aka the one with all the search results).
        """
        main_window = self.browser.window_handles[0]
        self.browser.switch_to.window(main_window)

    def maybe_add_thread_data(self, result_div, query, search_in_titles):
        """
        Conditionally add the new thread's info if the thread
        doesn't currently exist in self.thread_database.

        search_in_titles option is used to specify whether to include threads
        where the title doesn't contain the search query.

        Note that the thread will be opened in a new tab as a result of
        CTRL + 'T' on result_div, then closed after this method finishes.
        """
        thread_title = result_div.text
        if search_in_titles: # only search query in thread titles
            if query.upper() not in thread_title.upper(): return

        if thread_title not in self.thread_database:
            curr_thread = RFDThread(self.browser, result_div)
            self.thread_database[thread_title] = curr_thread.collect_data()

            curr_thread.browser.close()
            self.switch_to_main_window()

    def _aggregate_curr_page_results(self, query, search_in_titles):
        """
        Collect all search results on the current browser window.

        search_in_titles option is used to specify whether to include threads
        where the title doesn't contain the search query.
        """
        curr_page_results = self.browser.find_elements_by_xpath(RESULTS_LIST)
        # print(f'Total of {len(curr_page_results)} results on page {self.page_num} \n')
        for result_div in curr_page_results:
            self.maybe_add_thread_data(result_div, query, search_in_titles)

    def _aggregate_all_pages(self, query, search_in_titles):
        """
        Collect all search results (as list items) that appear in RFD search.
        Update self.thread_data, with key=title,
        and value=NamedTuple(URL, category, post date, upvote, downvote).

        search_in_titles option is used to specify whether to include threads
        where the title doesn't contain the search query.
        """
        total_pages = self._total_pages()
        while self.page_num <= total_pages:
            self._aggregate_curr_page_results(query, search_in_titles)

            # check if it's possible to visit the next page
            self.page_num += 1
            if self.page_num <= total_pages:
                self._go_to_page(self.page_num)
            else:
                break
