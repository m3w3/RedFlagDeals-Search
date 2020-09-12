from selenium.webdriver import Chrome
from RFDThread import *
from browser_settings import *
from constants import *


class RFDSearch:
    """
    The initialization module for RedFlagDeals search page using Chrome.
    (the individual search pages' interface)
    """

    def __init__(self, url):
        self.browser = Chrome(options=default_browser_options())
        # self.browser.implicitly_wait(10)
        self.URL = url
        self.total = 0
        self.page_num = 1
        self.thread_database = {}

        self._go_to_page(self.page_num)
        if not self._no_matches():
            self._aggregate_all_pages()
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
        main = self.browser.window_handles[0]
        self.browser.switch_to.window(main)

    def maybe_add_thread_data(self, result_div):
        """
        Conditionally add the new thread's info if the thread
        doesn't currently exist in self.thread_database.

        Note that the thread will be opened in a new tab as a result of
        CTRL + 'T' on result_div, then closed after this method finishes.
        """
        thread_title = result_div.text
        if thread_title not in self.thread_database:
            curr_thread = RFDThread(self.browser, result_div)
            # sleep(0.5)
            self.thread_database[thread_title] = curr_thread.collect_data()

            curr_thread.browser.close()
            self.switch_to_main_window()

    def _aggregate_curr_page_results(self):
        """
        Collect all search results on the current browser window.
        """
        curr_page_results = self.browser.find_elements_by_xpath(RESULTS_LIST)
        # print(f'total of {len(curr_page_results)} results \n')
        self.total += len(curr_page_results)
        for result_div in curr_page_results:
            self.maybe_add_thread_data(result_div)

    def _aggregate_all_pages(self):
        """
        Collect all search results (as list items) that appear in RFD search.
        Update self.thread_data, with key=title,
        and value=NamedTuple(URL, category, post date, upvote, downvote).

        Note:
        RFD search results has this weird bug where it'll say the results
        take up 'n' number of pages, but in fact it might take up
        less than 'n' (i.e. 20 pages, but only 14 contain results,
        and the remaining 6 pages are just empty).
        """
        total_pages = self._total_pages()
        while self.page_num <= total_pages:
            self._aggregate_curr_page_results()

            # check if it's possible to visit the next page
            self.page_num += 1
            if self.page_num <= total_pages:
                self._go_to_page(self.page_num)
            else:
                break
