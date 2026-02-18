# 4-10 Slices Assignment

# Guest list
guests = ["Defne", "Sirma", "Janet", "Cansel", "Elizabeth", "Mary"]

# Sort the list
guests.sort()

# Print the sorted guest list
print("Sorted guest list:")
for guest in guests:
    print(guest)

# --- SLICES ---
# First three items
print("\nThe first three items in the list are:")
first_three = guests[:3]
print(first_three)

# Three items from the middle
middle_index = len(guests) // 2  # orta index
middle_three = guests[middle_index-1:middle_index+2]  # orta üçlü
print("\nThree items from the middle of the list are:")
print(middle_three)

# Last three items
print("\nThe last three items in the list are:")
last_three = guests[-3:]
print(last_three)

# Naming the slices
print("\nNames of each slice:")
print("first_three:", first_three)
print("middle_three:", middle_three)
print("last_three:", last_three)
