# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:55:40 2019

@author: stany
"""


from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()