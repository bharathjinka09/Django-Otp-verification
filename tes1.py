from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



# x=random_with_N_digits(3)

x=123
otp =123

if(otp == x ):
    print('verified')




