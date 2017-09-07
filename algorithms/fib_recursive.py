def fibRecursive( user_input ):

    if user_input <= 1:
        return 1
    else:
        return fibRecursive( user_input - 1 ) + fibRecursive( user_input - 2 )

user_input = input()

print( fibRecursive( int( user_input ) ) )
