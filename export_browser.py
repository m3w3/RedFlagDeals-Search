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
    Add the HTML table header tag '<th></th>' to the element,
    which should be a string.
    """
    assert type(element) == str
    HTML_TABLE_HEADER[1] = element
    return "".join(HTML_TABLE_HEADER)


def make_table_data(element):
    """
    Add the HTML table data tag '<td></td>' to the element,
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


def make_html_row(col1_data, remaining_data, first_row=False):
    """
    *This is just 1 row.

    Given a column 1 data and an iterable remaining columns,
    add a HTML table data tag to each
    and arrange all of them into 1 HTML table row.
    """
    if first_row:  # this contains only headers for rest of the data
        HTML_TABLE_ROW[1] = "".join([make_table_header(col1_data)] +
                                    [make_table_header(remaining_data[i])
                                     for i in range(len(remaining_data))])
    else:
        assert type(remaining_data) == Thread
        hyperlink_title = make_html_link(remaining_data.url, col1_data)
        HTML_TABLE_ROW[1] = "".join([make_table_data(hyperlink_title)] +
                                    [make_table_data(remaining_data[i])
                                     for i in range(1, len(remaining_data))])
    return "".join(HTML_TABLE_ROW)


def make_html(rfd_data):
    """
    Create the HTML document, given {thread_title: Thread}.
    """
    header_row = [make_html_row(HEADER_0, HEADER_1, first_row=True)]
    data_row = [make_html_row(title, rfd_data[title]) for title in rfd_data]
    return "".join(HTML_HEAD + header_row + data_row + HTML_END)
