users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
def login(users):
    while True:
        a = input("User: ")
        b = input("Password: ")
        if a in users and users[a]==b:
            return a
            break
        else:
            print("Invalid username or password")

a = login(users1)

print(f"Welcome {a}")