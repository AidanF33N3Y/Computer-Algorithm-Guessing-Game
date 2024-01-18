import random

def computer_alg(x):
    high = x + 2
    low = 0
    guess = high / 2
    #r = int(input("Please insert Number from 1 to 1000: "))
    try:
        r = int(input("Please insert a number from 1 to 1000: "))
        if r not in range(1, 1001):
            print("No, you need to insert a number within the range (1 - 1000)")
        else:
            print(f"You inserted the number: {r}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    
    
    while r != guess:
        
        print(f'The Computer Guessed {guess}')
        if guess == r :
            print("Fucking thing guessed it.")
            print(f'The Computer Guessed {r}')
            break
        elif guess < r:
            low = guess
            low_2 = ((high - low) / 2) + low
            print(f'The new low bound is {low} and the value you guessed, {guess}, was wrong.')
            guess = int(low_2)
            if guess == r:
                print("Fucking thing guessed it.")
                print(f'The Computer Guessed {r}')
                break
        else:
            high = guess 
            high_2 =((high - low) / 2) + low
            print(f'The new high bound is {high} and the value you guessed, {guess}, was wrong.')
            guess = int(high_2)
            if guess == r:
                print("Fucking thing guessed it.")
                print(f'The Computer Guessed {r}')
                break
            
computer_alg(1000)
# def rand(x):
#     r = random.randint(1,x)
#     return r
            
# def game(x):
#     high = x
#     low = 0

#     r = rand(x)
#     guess = None
#     while guess != r:
#         guess = input(f"Make a guess from 0 - {x}: ")
#         if r == int(guess):
#             print(f'You Guessed the Value: {r}')
#             break
#         elif r >= int(guess):
#             print(f'Your guess is too low')
#         else:
#             print(f'Your guess is too high')
#     print("You Win Go Home")


