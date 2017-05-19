#definiton to reverse string
def stringRev(string):
    newstring = []
    for c in range(len(string)):
        newstring.insert(0, string[c])
    return ("".join(newstring))
