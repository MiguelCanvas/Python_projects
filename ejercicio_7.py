# // Clock shows h hours, m minutes and s seconds after midnight.

# // Your task is to write a function which returns the time since midnight in milliseconds.

# // h = 0
# // m = 1
# // s = 1

# // result = 61000

def hour(h,m,s):
    h*=3600000
    m*=60000
    s*=1000

    return h + m +s


print(hour(0,1,1))