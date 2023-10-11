users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def loggain():
    while True:
        a = input("User: ")
        b = input("Password: ")
        if a in users and users[a]==b:
            print(f"Welcome {users[a]}")
            break
        else:
            print("Invalid username or password")
loggain()