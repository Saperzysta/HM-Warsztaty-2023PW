import json
from pathlib import Path

path = Path("persons.json")

if path.exists():
    f = open(path, "r")
    persons = json.load(f)
    f.close()
else:
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
    answer = input("Do you want to continue Y/N? ")
    while answer.lower() not in ["y", "n"]:
        print("Choose Y or N only")
        answer = input("Do you want to continue Y/N? ")

    if answer.lower() =="n":
        f = open("persons.json", "w")
        json.dump(persons, f)
        f.close()
        break