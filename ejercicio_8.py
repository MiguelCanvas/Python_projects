# // You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# // Array can contain numbers or strings. X can be either.

# // Return true if the array contains the value, false if not.


array = ['la','dona','e','mobile','cual']

def check(a,x): #"a" hace referencia al array y "x" al elemento dentro del array
    if x in a:
        return True
    else:
        return False    


print(check(array,'hello'))        