# First Guest List
guests = ["Dasan Lucido", "Canet Carcar", "Defne Isanc"]

for guest in guests:
    print("Dear " + guest + ", you are invited to dinner!")

print("\nGood news! I found a bigger dinner table!")

# Updated Guest List
guests.insert(0, "Sirma Oztas")
guests.insert(3, "Cansel Kalkandelen")
guests.append("Ali Deran")

guests.sort()

for guest in guests:
    print("Dear " + guest + ", you are invited to dinner!")