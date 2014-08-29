#!/usr/bin/env python

"""
NLUlite is a high-level Natural Language Understanding
framework. 

This file is an example of the framework. This file is released with
BSD license.
"""

__author__  = 'NLUlite'
__version__ = '0.0.3'
__license__ = 'BSD'


from NLUlite import ServerProxy, Wisdom, Writer

server   = ServerProxy('localhost', 4001)
wisdom   = Wisdom(server)
wisdom.add('David is happy. If a person is happy, he smiles.')
answer   = wisdom.ask('Who smiles?')

print answer.comment()
for item in answer.elements():
    print item.comment()
