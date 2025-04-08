from secrets import randbits
import math 

def is_prime(n):
    if(n <= 1):
        return False
    for i in range (2, int(math.sqrt(n)) + 1): 
        if (n % i == 0):
            return False
    return True

def large_prime_gen(bits):
    while True:
        temp = randbits(bits)
        temp |= (1 << bits - 1 ) | 1 #interesting bit manipulation that sets first bit to 1 
        if(is_prime(temp)):#then shifts left by bits -1 positions and sets last bit to 1 so its odd
            return temp

if (__name__ == '__main__'):
    plaintext = 'godgamer'
    p = large_prime_gen(32)
    q = large_prime_gen(32)
    print(f"p == {p},   q: {q}" )
