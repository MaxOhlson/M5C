options = {"a":"Add item", "l":"List items", "q":"Log out"}

def view(description, strings):
    print(description)
    i = 1
    for x in strings:
        print (x + ") " + options[x])
        
view("Select an action",options)

while True:
    a = input("Option: ")
    if a in options:
        print(f"You selected option {a}) {options[a]}")
        break
    