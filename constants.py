"""
Pre-specified xPaths for RedFlagDeals website and other constants.
"""
# xpaths for unique elements
CATEGORIES = "//li[@class='thread_category']/a[@rel='nofollow']"
UPVOTES = "//div[@class='thread_header_actions_container']//span[" \
          "@class='upvote_count'] "
DOWNVOTES = "//div[@class='thread_header_actions_container']//span[" \
            "@class='downvote_count'] "
TOTAL_SEARCH_COUNT = '//span[@id="section_link_nb_forums"]'
TOTAL_PAGES = '//li[@id="pagination_forums"]//span[@class="pagination_total"]'

# xpaths for non-unique elements
RESULTS_LIST = "//h2[@class='title']/a[@class='search']"
FIRST_PAGE_LIST = "//a[@class='pagination_first pagination_button']"
PAGE_NUM_LIST = "//a[@class='pagination_menu_trigger']"
POST_TIME_LIST = "//span[@class='dateline_timestamp']"

# String add-on for user prompt
EXTRA_INFO = "(YYYY-MM-DD, or '31D', '12M', '1Y'): "

# Default RedFlagDeals search URL to modify
URL_ = 'https://www.redflagdeals.com/search/#!/q=Q/t=custom/s=forums/tf=TF/tt' \
       '=TT/p= '

# Used by export_browser.py
HTML_FILE = "RFD_Results.html"
HEADER_0 = 'Thread Title'
HEADER_1 = ['Category', 'Date Posted', 'Upvotes', 'Downvotes']
HTML_TABLE_HEADER = ["\n        <th>", None, "</th>"]
HTML_TABLE_DATA = ["\n        <td>", None, "</td>"]
HTML_TABLE_ROW = ['\n    <tr>', None, '\n    </tr>']
HTML_HYPERLINK = ["<a href=", None, ">", None, "</a>"]

# String to be printed
FOR_USER = \
    """
Instead of entering an exact date, you can enter a relative day from today.
Using: [digit][D, M, Y] as an input, you can specify the day from today.
For example:
    - 1D = 1 day before today
    - 12M = 12 months before today
    - 1Y = 1 year before today
    * 0D = today
"""
