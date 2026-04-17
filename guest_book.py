filename = "guest_book.txt"

print("Enter your name (type 'q' to quit):")

while True:
    name = input("Your name: ")
    
    if name.lower() == 'q':
        print("Goodbye!")
        break
    
    print(f"Hello, {name}! Welcome!")
    
    with open(filename, 'a') as file:
        file.write(name + "\n")