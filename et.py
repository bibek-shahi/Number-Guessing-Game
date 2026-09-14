import random

print(f'''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.\n\n''')

print(f'''Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n\n''')

diff_lvl = int(input("Enter the difficulty level: "))

is_valid=''
chance=''
count=0
guess=''
cr_nu=random.randint(1,100)


if diff_lvl == 1:
    diff_lvl= "Easy"
    chance = 10
    is_valid = True

elif diff_lvl == 2:
    diff_lvl= "Medium"
    chance = 5
    is_valid = True

elif diff_lvl == 3:
    diff_lvl= "Hard"
    chance = 3
    is_valid = True

else:
    print("\n\nPlease enter a valid difficulty level.")

if is_valid:
    print(f"\n\nGreat! You have selected the {diff_lvl} difficulty level.\nLet's start the game!\n\n")
    while count < chance:
        count = count + 1
        guess = int(input("Guess the number: "))
        if guess == cr_nu:
            print(f"Congratulations! You guessed the correct number in {count} attempts.")
            break
        else:
            if guess < cr_nu:
                print(f"Incorrect! The number is greater than {guess}.")
            else:
                print(f"Incorrect! The number is less than {guess}.")

