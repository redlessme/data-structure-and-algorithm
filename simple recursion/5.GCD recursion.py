#Write a program to compute the greatest common divisor (GCD) of two positive numbers

def gcd(a,b):
    if a<b:  #make sure a>=b
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)


print(gcd(4,10))


#gcd(a, b) = gcd(b, a mod b)