import random

# list with 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# randomly select 4 numbers and 1 letter
numbers = random.sample(items[:10], 4)
letter = random.choice(items[10:])

lottery = numbers + [letter]

print("Winning combination:", lottery)

# get user input
user_input = input("Enter 4 numbers and 1 letter separated by spaces: ")
user_list = user_input.split()

# convert first 4 inputs to integers
user_numbers = list(map(int, user_list[:4]))
user_letter = user_list[4]

user_combination = user_numbers + [user_letter]

# compare
if user_combination == lottery:
    print("Congratulations! You are a winner!")
else:
    print("Sorry, you did not win.")