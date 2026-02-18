# guest_list.py
# Initial and updated guest list

# Initial guest list
guests = ["Dasan Lucido", "Canet Carcar", "Defne Isanc"]

# Print initial invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

print("\nGood news! I found a bigger dinner table!")

# Updated guest list
guests.insert(0, "Sirma Oztas")
guests.insert(3, "Cansel Kalkandelen")
guests.append("Ali Deran")

# Sort the list alphabetically
guests.sort()

# Print updated invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")
