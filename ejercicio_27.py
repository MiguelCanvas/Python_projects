# // Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# // Examples
# // "This is an example!" ==> "sihT si na !elpmaxe"
# // "double  spaces"      ==> "elbuod  secaps"

def reverseWord(string):
    newString = list(string.split(" "))
    newList = []

    for x in newString:
        newList.append(x[::-1])

    nuevaVariable = " "

    return nuevaVariable.join(newList)


print(reverseWord("This is an example!"))



