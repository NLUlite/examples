#!/usr/bin/env python

"""
NLUlite is a high-level Natural Language Understanding
framework. 

This file is an example of the framework. This file is released with
BSD license.
"""

__author__  = 'NLUlite'
__version__ = '0.1.4'
__license__ = 'BSD'


from NLUlite import ServerProxy, Wisdom

server   = ServerProxy()
wisdom   = Wisdom(server)
wisdom.load('fetched.wisdom')
answer  = wisdom.ask('what happens where')

print answer.comment()
for item in answer.elements():
    print item.comment()
        
