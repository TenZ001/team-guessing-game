import random
import time

start_time = time.time()  
while True:  
    number = random.randint(1, 100) 
    print("Guess a number between 1 and 100")
    guess = int(input())
    if guess < number:  
        print("Too low!")
    elif guess > number:
        print("Too high!")
    if guess == number:
        print("You win!")
    else:
        print(f"Wrong! The number was {number}")
    print(f"Time taken: {time.time() - start_time:.2f}s")  
    print("Play again? (y/n)")
    if input().lower() != 'y': 
        break
