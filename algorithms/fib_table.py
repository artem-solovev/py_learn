def fibTable( user_input ):
    user_input = int( user_input )
    arr = [0,1]

    for i in range( 2, user_input + 1 ):
        arr.append( arr[i-1] + arr[i-2] )

    return arr

user_input = input()

user_input = int( user_input )

result = fibTable( user_input )

print( result[user_input] )
