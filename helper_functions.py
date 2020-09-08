from collections import namedtuple
from constants import *
"""
Helper functions for either RFDSearch or RFDThread.
"""

# Custom NamedTuple
Thread = namedtuple('Thread', 'url category date upvote downvote')
UserInput = namedtuple('UserInput', 'search_query start_date end_date')

def remove_post_id_from_url(url):
    """
    Removes the #p12311231 string in the last part of a RFD thread URL.
    """
    return url[:url.find('#')]

def generate_url(user_input):
    """
    Generate the RedFlagDeals search page URL based on the user's
    input for search term, start date, and end date.
    """
    correspond = zip(['Q', 'TF', 'TT'], user_input)
    for key, value in correspond:
        URL = URL_.replace(key, value)
    return URL

def RFD_results_empty(database, user_input):
    """
    Return True if the scrapped database is empty.

    Return an error message to user in case of empty search results.
    """
    assert type(user_input) == UserInput
    if bool(database):
        return False
    else:
        print(f"No results for '{user_input[0]}' " +
              f"between dates {user_input[1]} and {user_input[2]}")
        return True
