#  The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

#  Given a year, return the century it is in.

#  1705 --> 18
#  1900 --> 19
#  1601 --> 17
#  2000 --> 20


def century(year):
    i = 1
    count = 0
    while i <= year:
        i+= 100
        count+=1
    return count    


print(century(2000))        