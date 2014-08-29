from NLUlite import ServerProxy, Wisdom

server   = ServerProxy('localhost', 4001)
wisdom   = Wisdom(server)
wisdom.load('~/NLUlite/wisdoms/common.wisdom')
wisdom.add('David sells a car to Maria')
answer   = wisdom.ask('Who buys what from whom?')

print answer.comment()
for item in answer.elements():
    print item.comment()

