title = "Select an action"
options = {"a":"Add item", "l":"List items", "q":"Log out"}
options2 = {"r":"Try again", "q":"Quit"}

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

#menu(title, "What do you want to do? ", options)
#