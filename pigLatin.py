# program to take first constonant, move it to the end and add "ay"
string = "enter string"
appends = []
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
if string[0] in "aeiou":
    newstring = string + "-ay"
else:
    newstring = string[1:] + string[0] + "ay"
print(newstring)
