# // Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# // If you want to know more: http://en.wikipedia.org/wiki/DNA

# // In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# // More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# // Example: (input --> output)

# // "ATTGC" --> "TAACG"
# // "GTAT" --> "CATA"


# adn = "GTAT"

# x = list(adn)
# newArray = []
# adnFinal = ""

# for letra in x:
#     if letra == "A":
#         letra = "T"
#         newArray.append(letra)
#     elif letra == "T":
#         letra = "A"
#         newArray.append(letra)
#     elif letra == "C":
#         letra = "G"
#         newArray.append(letra)
#     elif letra == "G":
#         letra = "C"
#         newArray.append(letra)
#     print(letra)

# print(adnFinal.join(newArray))

def dnaConvert(adn):
    x = list(adn)
    newList = []
    adnFinal = ""

    for letter in x:
        if letter == "A":
            letter = "T"
            newList.append(letter)
        elif letter == "T":
             letter = "A"
             newList.append(letter)
        elif letter == "G":
             letter = "C"
             newList.append(letter)
        elif letter == "C":
             letter = "G"
             newList.append(letter)

    return adnFinal.join(newList)


print(dnaConvert("GTAT"))