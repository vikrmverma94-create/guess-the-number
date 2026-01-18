import random
secret_number=random.randint(1,10)
attempts=3

for i in range(attempts):
    guess=int(input("guess the number between 1 to 10 ,you have 3 attempts in total:"))
    if guess==secret_number:
        print("congratulations! you guessed it right.")
        break
    else:
        if i<attempts-1:
            print("wrong guess. try again.")
        else:
            print(f"sorry, you've used all attempts. the number was {secret_number}.")