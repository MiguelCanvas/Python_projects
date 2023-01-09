# // Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# // Examples:

# // solution('abc', 'bc') // returns true
# // solution('abc', 'd') // returns false


def sameLetters(array1,array2):
    count = 0
    newCount = 0

    array1 = list(array1)
    array2 = list(array2)

    res1 = array1[::-1]
    res2 = array2[:: -1]
    
    while count < len(res2):
        if res2[count] == res1[count]:
            newCount+=1
            
        count+=1

    if newCount == len(res2):
        return True
    elif newCount != len(res2):
        return False


print(sameLetters('miguel','uel'))

