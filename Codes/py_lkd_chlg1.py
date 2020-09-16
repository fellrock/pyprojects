# Detecting prime numbers

# Function formation:

def get_prime(num):
    factors=list()
    divisor=2
    while (divisor <= num):
        if (num%divisor)==0:
            factors.append(divisor)
            num=num/divisor
        else:
            divisor+=1        
    return factors



