# // Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# // The binary number returned should be a string.

# // Examples:(Input1, Input2 --> Output (explanation)))

# // 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# // 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)




def aBinario(num1,num2):
    res = num1 + num2
    newList = []
    newNumber = 0
    while res >= 1:
        newNumber = res%2
        res = res/2
        newList.append(int(newNumber))

    newList = newList[::-1]
    finalNumber  ="".join(map(str,newList))

    return int(finalNumber)



print(aBinario(1,1))
