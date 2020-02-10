"""
app.py for wilsonmcdade/kindhub
app.py reads a given config file and imports enabled widgets.
Author: Wilson McDade
"""

from flask import Flask, render_template
from configreader import reader
import os
import importlib
import sys

app = Flask(__name__)

def build_import(widgets):
    """
    Builds a list of enabled widget names for the import function below to use
    """

    imports = []

    for widget in widgets.values():
        wid = 'widgets.'+widget['name']
        imports.append(wid)

    return imports

def build_widgets(widgets):
    """
    Builds a dictionary of widgets for <widget>.py to use
    """

    enabled_widgets = {}

    for widget in widgets.values():
        if widget['enabled'] == 'true':
            enabled_widgets[widget['name']] = widget

    return enabled_widgets

if __name__ == '__main__':
    """
    Imports relevant widgets based on a provided config file.
    Runs the flask app.
    """

    if len(sys.argv) > 1 and sys.argv[1][-5:] == ".conf" :
        widgets = reader(sys.argv[1])
    else:
        widgets = reader("config.conf")

    enabled_widgets = build_widgets(widgets)

    to_import = build_import(enabled_widgets)

    for widget in to_import:
        importlib.import_module(widget)

    app.run("0.0.0.0",port="8080")
