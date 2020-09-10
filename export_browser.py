import webbrowser
from helper_functions import *


class ExportToHTML:
    """
    Creates an HTML table (using data scrapped with ChromeDriver),
    and saves it in an HTML file.
    """

    def __init__(self, database):
        assert len(database) > 0
        assert all([type(database[key]) == Thread for key in database])
        self.database = database

        with open(HTML_FILE, 'w') as html:
            html.write(make_html(self.database))
        webbrowser.open(HTML_FILE)


def make_table_header(element):
    """
    Add the HTML table header tag to the element,
    which should be a string.
    """
    assert type(element) == str
    HTML_TABLE_HEADER[1] = element
    return "".join(HTML_TABLE_HEADER)


def make_table_data(element):
    """
    Add the HTML table data tag to the element,
    which should be a string.
    """
    assert type(element) == str
    HTML_TABLE_DATA[1] = element
    return "".join(HTML_TABLE_DATA)


def make_html_link(url, text):
    """
    Using the provided url,
    return the html hyperlink attribute with the text.

    e.g. <a href="url">text</a>
    """
    assert type(url) == str and type(text) == str
    HTML_HYPERLINK[1] = url
    HTML_HYPERLINK[3] = text
    return "".join(HTML_HYPERLINK)


def make_html_row(title, data, data_row=True):
    """
    Given a thread_title and an iterable thread_data,
    add a HTML table data tag to each
    and arrange all of them into 1 HTML table row.
    """
    if data_row:
        assert type(data) == Thread
        title_with_link = make_html_link(data.url, title)
        HTML_TABLE_ROW[1] = "".join([make_table_data(title_with_link)] +
                                    [make_table_data(data[i])
                                     for i in range(1, len(data))])
    else:
        HTML_TABLE_ROW[1] = "".join([make_table_header(title)] +
                                    [make_table_header(data[i])
                                     for i in range(len(data))])
    return "".join(HTML_TABLE_ROW)


def make_html(rfd_data):
    """
    Create the HTML document, given {thread_title: Thread}.
    """
    html_start = "<html>\n<table>"
    table_header = make_html_row(HEADER_0, HEADER_1, data_row=False)
    table_data = [make_html_row(title, rfd_data[title])
                  for title in rfd_data]
    html_end = "\n</table>\n</html>"
    return "".join([html_start, table_header] + table_data + [html_end])
