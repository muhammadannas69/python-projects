import random
number=random.randint(1,10)
attempt = 0
while True:
    try:
        guess = int(input("Enter a number"))
        attempt +=1      
        if number > guess:
            print("enter larger")
            guess_of = guess
        elif number < guess:
            print("enter lower ")
        elif number == guess:
            print(f"you guess correct in {guess} attempt {attempt}" )
            break
    except ValueError:
        print("please Enter a number")