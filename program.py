persons = {}
commands = [
    "new_contact", "show_contacts"
]
while True:
    command = input("Peek an option: new_contact, show_contacts: ")
    while command not in commands:
        print("Unknown command, try again")
        command = input(f"Peek an option: {commands} ")
    if command == "new_contact":
        name = input("Name: ")
        number = input("Phone Number: ")
        persons[name] = number
    elif command == "show_contacts":
        print(persons)
    #else:
     #   print("unknown command")
    command = input("Do you want to continue Y/N? ")
    if command =="N":
        break