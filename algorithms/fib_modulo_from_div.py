def fibTable( user_input ):
    user_input = int( user_input )
    arr = [0,1]

    for i in range( 2, user_input + 1 ):
        arr.append( ( arr[0] + arr[1] ) % 10 )
        del arr[0]

    return arr

user_input, divider = input().split( ' ' )

result = fibTable( user_input )

if divider <= 2:
    break

#print( ( result[ len( result ) - 1 ] ) % int( divider ) )

print( ( result[ len( result ) - 1 ] ) % int( divider ) )
