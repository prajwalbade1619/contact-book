contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!\n")

def view_contact_list():
    print("\nContact List:")
    for name, contact_info in contacts.items():
        print(f"{name}: {contact_info['phone_number']}")

def search_contact():
    search_term = input("Enter contact name or phone number to search: ")
    found_contacts = []

    for name, contact_info in contacts.items():
        if search_term.lower() in name.lower() or search_term in contact_info['phone_number']:
            found_contacts.append((name, contact_info))

    if found_contacts:
        print("\nSearch Results:")
        for name, contact_info in found_contacts:
            print(f"{name}: {contact_info['phone_number']}")
    else:
        print("No contacts found matching the search term.")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print(f"Current contact details for '{name}': {contacts[name]}")
        new_phone_number = input("Enter new phone number (press Enter to keep the current one): ")
        new_email = input("Enter new email address (press Enter to keep the current one): ")
        new_address = input("Enter new address (press Enter to keep the current one): ")

        if new_phone_number:
            contacts[name]['phone_number'] = new_phone_number
        if new_email:
            contacts[name]['email'] = new_email
        if new_address:
            contacts[name]['address'] = new_address

        print(f"Contact '{name}' updated successfully!\n")
    else:
        print(f"Contact '{name}' not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"Contact '{name}' not found.\n")

def display_menu():
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
