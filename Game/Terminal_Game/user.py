#!/usr/bin/python3
""" This file is the declarative user class
"""

import random


class User:
    """ This is Representation class user"""
    id = random.randint(0,100)
    score = 0
    nickname = ""
