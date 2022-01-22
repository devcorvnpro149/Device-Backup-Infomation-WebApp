import dash_html_components as html
from navbar import create_navbar, create_navbar2

nav = create_navbar2()

header = html.H3('Welcome to page 3!')


def create_page_3():
    layout = html.Div([
        nav,
        header,
    ])
    return layout