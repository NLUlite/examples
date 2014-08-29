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


from NLUlite import ServerProxy, Wisdom, Writer

server    = ServerProxy('localhost', 4001)
wisdom   = Wisdom(server)
wisdom.add('The chancellor had planned to go to Berlin January 10, 2102.')
answer   = wisdom.ask('is someone going to Germany?')
## answer   = wisdom1.ask('who goes to Berlin?')

# Print a comment to all the answers
writer= Writer(wisdom)
print writer.write(answer)

for item in answer.elements():
    print writer.write(item)


