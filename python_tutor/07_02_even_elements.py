import sys

arr = sys.argv[1].split()

#print( arr )

for elem in arr :
    if int( elem ) % 2 == 0:
        print( elem, end=" " )
