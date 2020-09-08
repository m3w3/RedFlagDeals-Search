from selenium.webdriver.common.keys import Keys
from time import sleep
from constants import *
from helper_functions import *

class RFDThread:
    """
    The initialization module for RedFlagDeals thread using Chrome.
    (the individual threads' interface)
    """

    def __init__(self, browser, result_div):
        self.browser = browser
        self.result_div = result_div
        
        self._new_tab_for_thread()
        self._go_to_page_one()

    def _new_tab_for_thread(self):
        """
        Create a new tab in the provided browser,
        using the given thread header div from the results page.
        """
        # open link in new tab -> switch to new tab
        self.result_div.send_keys(Keys.CONTROL + Keys.RETURN)
        self.browser.switch_to.window(self.browser.window_handles[1])        
    def _go_to_page_one(self):
        """
        Go to page 1 of the RFD thread.

        3 possibilites:
        1) Browser not on page 1
        2) Browser on page 1, but thread has more than 1 page
        3) Browser on page 1, and thread only has 1 page

        Note that this clickable button will only exist
        if the thread opened is currently NOT on page 1.
        If it's on page 1, it'll not exist.
        Also, the button to click will always be the first element in the list above
        """
        first_page_button_list = self.browser.find_elements_by_xpath(FIRST_PAGE_LIST)
        if len(first_page_button_list) != 0: # check if not on page 1
            first_page_button_list[1].click()
        else:
            url = self.browser.current_url
            if '#' in url: return self.browser.get(remove_post_id_from_url(url))

    def collect_data(self):
        """
        Return the following info about the current thread, and return as a named tuple:
        1) thread category
        2) thread's initial post time
        3) thread's total upvotes
        4) thread's total downvotes
        5) thread's total score (aka upvotes - downvotes)
        """
        return Thread(self.browser.current_url,
                      self.browser.find_element_by_xpath(CATEGORIES).text,
                      self.browser.find_elements_by_xpath(POST_TIME_LIST)[0].text,
                      self.browser.find_element_by_xpath(UPVOTES).text,
                      self.browser.find_element_by_xpath(DOWNVOTES).text)
