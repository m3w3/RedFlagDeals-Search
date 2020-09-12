# RedFlagDeals-Search
Search for unique forum posts on RedFlagDeals.

# Why?
As of now, if you try searching for a keyword in the titles of any RedFlagDeals' threads, you'll end up with something like this: https://www.redflagdeals.com/search/#!/q=headphone/t=any/s=forums/p=1. The search will be performed on a per comment basis, so you'll end up with many results of the same thread.
The purpose of this program is to scrape all the search results using Selenium Webdriver, and consolidate them into one easily-accessible table in HTML with the option to sort the results.

# Setting Up Selenium
Download the Python binding for Selenium:
```Python
pip install selenium
```

Get the latest ChromeDriver here: https://sites.google.com/a/chromium.org/chromedriver/downloads

The API for Python Webdriver can be found here: https://selenium-python.readthedocs.io/api.html

# Features to Add/Implement (TODOs):
- Use Wait instead of sleep()
- Use CSS selector instead of xPath to retrieve web elements. This should allow the program to work properly in headless Chrome mode.
