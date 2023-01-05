run = True
while (run):
    teststr = input("Palindrome or type exit: ")
    if teststr == "exit":
        run = False
        break

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    if newstr == newstr[::-1]:
        palindrome = True
    else:
        palindrome = False

    print("Palindrome is", palindrome)
