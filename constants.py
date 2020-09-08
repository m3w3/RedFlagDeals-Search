"""
Pre-specified xPaths for RedFlagDeals website and other constants.
"""
# xpaths for unique elements
CATEGORIES = "//li[@class='thread_category']/a[@rel='nofollow']"
UPVOTES = "//div[@class='thread_header_actions_container']//span[@class='upvote_count']"
DOWNVOTES = "//div[@class='thread_header_actions_container']//span[@class='downvote_count']"
TOTAL_SEARCH_COUNT = '//span[@id="section_link_nb_forums"]'
TOTAL_PAGES = '//li[@id="pagination_forums"]//span[@class="pagination_total"]'

# xpaths for non-unique elements
RESULTS_LIST = "//h2[@class='title']/a[@class='search']"
FIRST_PAGE_LIST = "//a[@class='pagination_first pagination_button']"
PAGE_NUM_LIST = "//a[@class='pagination_menu_trigger']"
POST_TIME_LIST = "//span[@class='dateline_timestamp']"

# String add-on for user prompt
EXTRA_INFO = "(YYYY-MM-DD, or '-31D', '-12M', '-1Y', or 'any'): "

# Default RedFlagDeals search URL to modify
URL_ = 'https://www.redflagdeals.com/search/#!/q=headphone/t=custom/s=forums/tf=2020-7-20/tt=2020-8-18/p='
# URL_ = 'https://www.redflagdeals.com/search/#!/q=Q/t=custom/s=forums/tf=TF/tt=TT/p='
