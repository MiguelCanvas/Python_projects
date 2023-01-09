# // Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# // The output should be two capital letters with a dot separating them.

# // It should look like this:

# // Sam Harris => S.H

# // patrick feeney => P.F


def Initials(name):
    name = name.upper()
    newList = name.split(" ")
    firstName = newList[0]
    secondName = newList[1]

    return(f"{firstName[0]}.{secondName[0]}")


print(Initials("Miguel Vasquez"))