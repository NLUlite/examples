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

server  = ServerProxy('localhost', 4001)
wisdom  = Wisdom(server)
wisdom.add('[% this is the description %] The chancellor is going to Berlin. If someone is happy and is satisfied he smiles.')
wisdom.save('test.wisdom')

