#!/usr/bin/env python
"""
NLUlite is a high-level Natural Language Understanding
framework. 

This file is an example of the framework. This file is released with
BSD license.
"""

__author__  = 'NLUlite'
__version__ = '0.1.0'
__license__ = 'BSD'



from NLUlite import ServerProxy, Wisdom

server  = ServerProxy('localhost', 4001)
w       = Wisdom(server)

w.add('The chancellor is going to Berlin.')
answer = w.ask('Who goes to Germany?')

print answer.comment()
for item in answer.elements():
    print item.text
    print item.description
    for pair in item.pairs:
        print pair.query + ':' + pair.reply

