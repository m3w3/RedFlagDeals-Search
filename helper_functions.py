from collections import namedtuple
from constants import *
from datetime import date, timedelta

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
    url = URL_
    for key, value in correspond:
        url = url.replace(key, value)
    return url


def rfd_results_empty(database, user_input):
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


def validate_date(input_date):
    """
    Date either must be in the format of either:
    1) YYYY-MM-DD
    2) [digit][day/month/year], e.g. '1D' or '3M'
    """
    length = len(input_date)
    if length == 2 or length == 3:
        return (input_date[:-1].isdecimal() and
                input_date[-1].lower() in ['d', 'm', 'y'])
    elif length == 10:
        date_list = input_date.split('-')
        try:
            date_list = [int(value) for value in date_list]
            date(year=date_list[0], month=date_list[1], day=date_list[2])
        except:
            print(f"Input '{input_date}' is invalid!")
        finally:
            return True

    return False


def standardize_date(input_date):
    """
    Converts 1M -> the date that's 1 month before today's current date,
    Or 30D -> the date that's 30 days before today's current date
    Or 1Y -> the date that's 1Y before today's current date
    ... etc.

    Return the exact date.

    If input_date doesn't need to be converted, return it instead.
    """
    length = len(input_date)
    if length != 2 and length != 3:
        return input_date

    alphabet = input_date.lower()[-1]  # i.e. '1D' --> 'd'
    multipliers = {'d': 1, 'm': 30.4167, 'y': 365}
    delta = timedelta(int(input_date[:-1]) * multipliers[alphabet])
    return str(date.today() - delta)
