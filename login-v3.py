users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
options2 = {"r":"Try again", "q":"Quit"}
def login(users):
    while True:
        a = input("User: ")
        b = input("Password: ")
        if a in users and users[a]==b:
            return a
            break
        else:
            print("Invalid username or password")
            b = menu("","Option: ", options2)
            if b ==  "q":
                break

def view(description, strings):
    print(description)
    for x in strings:
        print (x + ") " + strings[x])


def menu(title, prompt, options):
    view(title,options)
    while True:
        a = input(prompt)
        if a in options:
            print(f"You selected option {a}) {options[a]}")
            return a
            break
