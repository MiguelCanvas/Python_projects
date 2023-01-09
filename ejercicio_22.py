"""""// Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

// For example,

// [true,  true,  true,  false,
//   true,  true,  true,  true ,
//   true,  false, true,  false,
//   true,  false, false, true ,
//   true,  true,  true,  true ,
//   false, false, true,  true]
// The correct answer would be 17.

// Hint: Don't forget to check for bad values like null/undefined."""

newArray = [True,  True,  True,  False, True,  True,  True,  True ,
   True,  False, True,  False,
   True,  False, False, True ,
   True,  True,  True,  True , "", False, True,  True]




def isSheep(array):
    count = 0
    for x in array:
        if x == True:
            count+=1

    return count


print(isSheep(newArray))






