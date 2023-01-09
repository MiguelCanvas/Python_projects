# // Convert number to reversed array of digits
# // Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# // Example(Input => Output):
# // 35231 => [1,3,2,5,3]
# // 0 => [0]


number = 2019

newArray = [int(x) for x in str(number)]

newArray = list(reversed(newArray))

print(newArray)