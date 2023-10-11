strings = []
n = 3

def view(description, strings):
    print(description)
    i = 1
    for x in strings:
        print (str(i) + ") " + x)
        i = i + 1

def add(prompt,strings):
    for x in range (n):
        a = input(prompt)
        strings.append(a)
    
    return strings

add("Lägg till en sträng", strings)
view(f"Du har matat in följande {n} strängar", strings)
