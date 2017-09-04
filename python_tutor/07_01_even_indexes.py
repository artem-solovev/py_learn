import sys

arr = sys.argv[1]

for i in range( len( arr ) ):
    if i == 0 or i % 2 == 0:
        print( arr[i] )
