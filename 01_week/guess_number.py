import random

answer = random.randint( 0, 100 )

while True:
    attempt = input( "Guess number: " )

    if attempt == "" or attempt == "exit":
        break

    if not attempt.isdigit():
        print( "Enter the correct number!" )
        continue

    user_answer = int( attempt )

    if user_answer > answer:
        print( "The number is less than your" )
    elif user_answer < answer:
        print( "The number is more than your" )
    else:
        print( "That's right" )
        break
