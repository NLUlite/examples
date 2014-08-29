from NLUlite import ServerProxy, Wisdom, join_answers

server = ServerProxy()
wisdom = Wisdom(server)

wisdom.add('David might go to a pub. Tim already went there.')
answer=wisdom.ask('who will go to a pub')
print answer.comment()
for item in answer.elements():
    print item.comment()
