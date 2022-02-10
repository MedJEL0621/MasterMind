#!/usr/bin/python3
# layout is the templeate of the html
from templates.routes_temp.layout import layout

def index(name):
    """ This is one definition to first index
        to html response to server
    """
    html = layout(name)
    return html