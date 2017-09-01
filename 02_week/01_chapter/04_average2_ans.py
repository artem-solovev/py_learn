cnt = 0
sumValues = 0
numbers = []

lowest = 0
highest = 0

userInput = True

def simpleSorting( arr ):
    for i in arr:
        print( i )

    print( "Array length ", len( arr ) )

while ( userInput ):

    try:
        userInput = 0
        userInput = input( "enter a number or Enter to finish: " )

        if isinstance( userInput, int ):
            numbers.append( userInput )

        sumValues += int( userInput )

        print( "You've entered ", userInput )

        if 0 == cnt:
            lowest = int( numbers[cnt] )
        else:
            if int( numbers[cnt] ) > highest:
                highest = int( numbers[cnt] )

            if int( numbers[cnt] ) < lowest:
                lowest = int( numbers[cnt] )



        if not numbers[cnt]:
            break

        cnt += 1

    except ValueError as err:
        print( err )

        continue

mean = sumValues / cnt

simpleSorting( numbers )

print( "Sum ", sumValues )
print( "Cnt ", cnt )
print( "Mean ", mean )
print( "Highest number ", highest )
print( "Lowest number ", lowest )
