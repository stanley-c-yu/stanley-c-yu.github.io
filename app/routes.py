# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:42:44 2019

@author: stany
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"