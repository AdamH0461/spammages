# program to take first constonant, move it to the end and add "ay"
string = input("enter string")
appends = []
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
if string[0] not in vowels:
    appends[0] = string[0]
    if string[1]:
        appends[1] = string[1]
appends.append("-ay")
print(appends)
