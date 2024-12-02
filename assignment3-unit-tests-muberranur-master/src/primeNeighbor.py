'''
Created by Neda Topuz
Modified by Müberra Nur Açık
'''

def primeNeighbor(upperBound):
    # must be an integer, between 1 and 1000
    if not isinstance(upperBound, int) or upperBound <= 0 or upperBound > 1000:
        return 0

    # helper function to check ifprime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):  
            if n % i == 0:
                return False
        return True

    # If the upperBound itself is prime, return it
    if is_prime(upperBound):
        return upperBound

   
    for i in range(upperBound - 1, 1, -1):
        if is_prime(i):
            return i

   
    return 0
