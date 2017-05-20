# program to count number of vowels
original = input("enter string: ")
a, e, i, o, u = 0
vowellist = ""
vowels = "aeiou"
string = original.lower()
for c in range(string.len):
    char = string[c]
    if char == "a":
        a += 1
        vowellist += "a"
    elif char == "e":
        e += 1
        vowellist += "e"
    elif char == "i":
        i += 1
        vowellist += "i"
    elif char == "o":
        o += 1
        vowellist += "o"
    elif char == "u":
        u += 1
        vowellist += "u"
print(a, "as were found \n", e, "es were foundn\n", i, "is were found"
print(o, "os were found ")
