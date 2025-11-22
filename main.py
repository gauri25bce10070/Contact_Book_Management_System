contacts = []   # empty list to store contacts

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")
    contacts.append([name, phone, email])   # store data as list
    print("Contact Added Successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if len(contacts) == 0:
        print("No contacts available!")
    else:
        for c in contacts:
            print(f"Name: {c[0]} | Phone: {c[1]} | Email: {c[2]}")

def search_contact():
    print("\n--- Search Contact ---")
    name = input("Enter Name to Search: ")
    found = False
    for c in contacts:
        if c[0] == name:
            print(f"Name: {c[0]} | Phone: {c[1]} | Email: {c[2]}")
            found = True
            break
    if not found:
        print("Contact Not Found!")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter Name to Delete: ")
    found = False
    for c in contacts:
        if c[0] == name:
            contacts.remove(c)
            found = True
            print("Contact Deleted Successfully!")
            break
    if not found:
        print("Contact Not Found!")

# Menu
while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")
