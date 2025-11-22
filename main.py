contacts = []   # list to store all contacts

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")
    contacts.append([name, phone, email])
    print("Contact Added Successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:   # same as len(contacts)==0
        print("No contacts available!")
    else:
        for c in contacts:
            print(f"Name: {c[0]} | Phone: {c[1]} | Email: {c[0]}")

def search_contact():
    print("\n--- Search Contact ---")
    name = input("Enter Name to Search: ")
    for c in contacts:
        if c[0].lower() == name.lower():   # case-insensitive search
            print(f"Name: {c[0]} | Phone: {c[1]} | Email: {c[0]}")
            return
    print("Contact Not Found!")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter Name to Delete: ")
    for c in contacts:
        if c[0].lower() == name.lower():
            contacts.remove(c)
            print("Contact Deleted Successfully!")
            return
    print("Contact Not Found!")

# Main Menu
while True:
    print("\n===== CONTACT BOOK =====")
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
        print("Thank You for using Contact Book!")
        break
    else:
        print("Invalid Choice! Try Again.")
