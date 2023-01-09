# // Return the number (count) of vowels in the given string.

# // We will consider a, e, i, o, u as vowels for this Kata (but not y).

# // The input string will only consist of lower case letters and/or spaces.


theword = "constantinopla"


def vowelsCount(word):

    newWord = list(word)
    contador = 0
    for x in newWord:
        if(x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
            contador +=1

    return contador


print(vowelsCount(theword))

