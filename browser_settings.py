"""
Any settings of Chrome browser goes here.
"""
from selenium.webdriver.chrome.options import Options


def default_browser_options():
    """
    Return the default browser options for our webdriver.
    """
    opts = Options()
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--ignore-ssl-errors')
    # TODO: add support for headless option
    opts.headless = False
    return opts
