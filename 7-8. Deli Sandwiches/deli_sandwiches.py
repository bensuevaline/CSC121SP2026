# 7-8. Deli Sandwiches

sandwich_orders = ['tuna', 'turkey', 'veggie', 'ham', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches that were made:")

for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")