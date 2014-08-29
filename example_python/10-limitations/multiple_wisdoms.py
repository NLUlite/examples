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


from NLUlite import ServerProxy, Wisdom, join_answers

server = ServerProxy()
wisdom1 = Wisdom(server)
wisdom2 = Wisdom(server)

wisdom1.add('David goes to the cinema to see a movie')
wisdom2.add('Anna travels to Germany for business')

question = 'who goes where'

# Ask the question
answers1 = wisdom1.ask(question)
answers2 = wisdom2.ask(question)
answers = join_answers([answers1, answers2])
print answers.comment()
for item in answers.elements() :
    print item.comment()
