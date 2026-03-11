# 7-5. Movie Tickets

num_tickets = int(input("How many tickets would you like to buy? "))

count = 0
total_cost = 0

while count < num_tickets:
    age = int(input("Enter the age of the ticket holder: "))

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total_cost = total_cost + price
    count = count + 1

print("Total cost of the tickets: $" + str(total_cost))
