import random

DEFAULT_VALUE = 5

print( "__WELCOME TO VOGON POETRY__" )
print( "___________________________" )

articles = [ 'a', 'the', 'an' ]

nouns = ['time', 'person', 'year', 'way', 'day', 'thing', 'man',
'world', 'life', 'hand', 'part', 'child', 'eye', 'woman',
'place', 'work', 'week', 'case', 'point', 'government',
'company', 'number', 'group', 'problem', 'fact']

verbs = ['be', 'have', 'do', 'say', 'get', 'make', 'go',
'know', 'take', 'see', 'come', 'think', 'look',
'want', 'give', 'use', 'find', 'tell', 'ask',
'work', 'seem', 'feel', 'try', 'leave', 'call']

adverbs = ['quickly', 'cheerfully', 'painfully',
'easily', 'secretly', 'quietly','peacefully', 'cleverly',
'often', 'sometimes', 'every week', 'monthly', 'always',
'never', 'hourly', 'seldom', 'frequently', 'annually']

strSequence = [ articles, nouns, adverbs, verbs ]

try:
    userChoise = int( input( "Enter the number: " ) )
except ValueError as err:
    print( "\t___________________" )
    print( "Value by default is ", DEFAULT_VALUE )
    print( "\t___________________" )
    userChoise = DEFAULT_VALUE


for i in range( 0, userChoise ):
    randStr = ""

    for j in range( len( strSequence ) ):
        randStr += strSequence[j][ random.randint( 0, len( strSequence[j] ) - 1 ) ] + " "

    print( randStr )
