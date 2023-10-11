users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva","vante"], "bosse":["spik","skruv","hammare"], "stina":["tidsmaskin"]}

print ("Användare:")
print()
for user in users:
       print (f"{user}")
print()
def skrivut(users):
    for user in users:
        print (f"{user}" + ") " + f"{users[user]}")
print()
print("Användare och lösenord:")
print()
skrivut(users)
print()
print("Användare och deras data:")
print()
skrivut(data)

def lookup(a):
    if a in data:
        return data[a]
    else:
        return False

a = input("Slå upp en användare: ")
if lookup(a) == False:
    print(f"Användare {a} finns inte")
else:
    print(lookup(a))