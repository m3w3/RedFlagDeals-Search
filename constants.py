"""
Pre-specified xPaths for RedFlagDeals website and other constants.
"""
from datetime import *

# xpaths for unique elements
CATEGORIES = '//li[@class="thread_category"]/a[@rel="nofollow"]'
UPVOTES = '//div[@class="thread_header_actions_container"]//span[' \
          '@class="upvote_count"] '
DOWNVOTES = '//div[@class="thread_header_actions_container"]//span[' \
            '@class="downvote_count"] '
TOTAL_SEARCH_COUNT = '//span[@id="section_link_nb_forums"]'
TOTAL_PAGES = '//li[@id="pagination_forums"]//span[@class="pagination_total"]'
LOCKED = '//div[@class="thread_header_endmatter"]'

# xpaths for non-unique elements
RESULTS_LIST = '//h2[@class="title"]/a[@class="search"]'
FIRST_PAGE_LIST = '//a[@class="pagination_first pagination_button"]'
PAGE_NUM_LIST = '//a[@class="pagination_menu_trigger"]'
POST_TIME_LIST = '//span[@class="dateline_timestamp"]'

# String add-on for user prompt
EXTRA_INFO = '(YYYY-MM-DD, or "[integer][D/W/M/Y]" i.e. 2W): '

# Default RedFlagDeals search URL to modify
URL_ = f'https://www.redflagdeals.com/search/#!/q=Q/t=custom/s=forums/tt={str(date.today())}/tf=TF/p='
# Default URL of the script Sortable (used to sort HTML tables)
SORTABLE = 'https://www.kryogenix.org/code/browser/sorttable/sorttable.js'
# Used by export_browser.py
HTML_FILE = 'RFD_Results.html'
HEADER_0 = 'Thread Title'
HEADER_1 = ['Category', 'Date Posted', 'Upvotes', 'Downvotes']
HTML_HEAD = ['<html>', '\n<head>', '\n    <meta charset="utf-8">',
             '\n    <title>RedFlagDeals Search Results</title>',
             '\n    <link rel="stylesheet" type="text/css" href="style.css">',
             '\n</head>', '\n<body>', '\n    <table class="sortable">']
HTML_TABLE_HEADER = ['\n            <th>', None, '</th>']
HTML_TABLE_DATA = ['\n            <td>', None, '</td>']
HTML_TABLE_ROW = ['\n        <tr>', None, '\n        </tr>']
HTML_HYPERLINK = ['<a href=', None, '>', None, '</a>']
HTML_ALERT = ['\n    <script>',
              '\n        window.alert("Click on table header to sort!");',
              '\n    </script>']
HTML_END = ['\n    </table>',
            '\n    <script type="text/javascript" src="' + SORTABLE + '"></script>',
            '\n</body>', '\n</html>']

# Hashtable for dates
DATE_MAP = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

# String to be printed
FOR_USER = \
    """
Instead of entering an exact date, you can enter a relative day from today.
Using: [digit][D, W, M, Y] as an input, you can specify the day from today.
For example:
    - 1D = 1 day before today
    - 2W = 2 weeks before today
    - 12M = 12 months before today
    - 1Y = 1 year before today
    * 0D = today
"""

FOR_USER_2 = ("Disregard query results from comments "
              + "and search your query in thread titles only? (T/F) ")
