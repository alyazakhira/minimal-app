# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:34:37 2023

@author: Akira
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"