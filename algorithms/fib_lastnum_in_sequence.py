def fibTable( user_input ):
    user_input = int( user_input )
    arr = [0,1]

    for i in range( 2, user_input + 1 ):
        arr.append( ( arr[0] + arr[1] ) % 10 )
        del arr[0]

    return arr

user_input = input()

result = fibTable( user_input )

print( result[ len( result ) - 1 ] % 10 )
