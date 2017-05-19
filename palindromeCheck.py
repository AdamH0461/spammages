import stringReverse as sr
origin = input("enter Shenanigans")
reverse = sr.stringRev(origin)
if origin == reverse:
    print (origin + " reversed is " + reverse +"\n palindrome confirm")
else :
    print ("U GOT NO PALINDROME")
    print (origin + " reversed is " + reverse)

