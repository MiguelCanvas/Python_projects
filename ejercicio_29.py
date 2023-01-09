# // Complete the square sum function so that it squares each number passed into it and then sums the results together.

# // For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def squaredNumbers(number1,number2,number3):
    number1 = number1**2
    number2 = number2**2
    number3 = number3**2
    finalResult = number1 + number2 + number3
    
    return finalResult


print(squaredNumbers(1,2,2))
