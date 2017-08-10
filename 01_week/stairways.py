import sys

user_input = int( sys.argv[1] )
symbols = ""
spaces = ""

for space in range( user_input ):
    spaces += " "

for i in range( user_input ):
    symbols += "#"
    spaces = spaces[:-1]

    print( spaces + symbols + "\n" )
