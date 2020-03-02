# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:55:40 2019

@author: stany
"""

# This builds the static content to the project root 

from project import main

freezer = Freezer(app)

if __name__ == '__main__':
    main.freezer.freeze()