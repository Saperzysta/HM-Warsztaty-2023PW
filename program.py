persons = {}

while True:
    command = input("Peek an option: new_con, show_con: ")
    if command == "new_con":
        name = input("Name: ")
        number = input("Phone Number: ")
        persons[name] = number
    elif command == "show_con":
        print(persons)
    else:
        print("unknown command")
    command = input("Do you want to continue Y/N? ")
    if command =="N":
        break