from NLUlite import ServerProxy, Wisdom, WisdomParameters

server = ServerProxy()
wisdom = Wisdom(server)

wp= WisdomParameters()
wp.set_do_solver('true') # Rules are always applied
wisdom.set_wisdom_parameters(wp)

wisdom.add('Socrates is a man. If someone is a man he is mortal.')

answers = wisdom.ask("is socrates a mortal")
answer_comment = answers.comment()
item_comment   = ""
for item in answers.elements():
    item_comment += item.comment()

print answers.comment()
for item in answers.elements() :
    print item.comment()
