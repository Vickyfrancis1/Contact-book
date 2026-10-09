# CONTACT

contacts = {}

try:
    with open("contacts.txt", "r") as file:
        for line in file:
            name, number = line.strip().split(",")
            contacts[name] = number
except FileNotFoundError:
    pass

def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all")
    print("4. Delete")
    print("5. Quit")
    choice = input("Choose: ").strip()
    
    if choice == "1":
        name = input("Name: ").strip().title()
        number = input("Number: ").strip()
        contacts[name] = number
        print("Saved.")
        save_contacts()
    elif choice == "2":
        name = input("Search for: ").strip().title()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"{name} is not in your contacts.")
    elif choice == "3":
        for name, number in contacts.items():
            print(f"{name}: {number}")
            
    elif choice == "4":
        name = input("Delete who? ").strip().title()
        if name in contacts:
            del contacts[name]
            save_contacts()
            print(f"{name} deleted.")
        else:
            print(f"{name} is not in your contacts.")
            
    elif choice == "5":
        save_contacts()
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, 4, or 5")