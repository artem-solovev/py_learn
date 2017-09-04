import sys

arr = sys.argv[1].split()

for i in range( len( arr ) ):
    if i != 0 and int( arr[i] ) > int( arr[i-1] ):
        print( arr[i], end = " " )
