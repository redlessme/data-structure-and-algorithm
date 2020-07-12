def Gcd(a,b):#gcd(a, b) = gcd(b, a mod b)
    if a<b:
        a,b=b,a
    while b != 0:
        temp = a%b
        a=b
        b=temp
    return a

    #gcd(120, 45) = gcd(45, 120 % 45) = gcd(45, 30)
    #gcd(45, 30) = gcd(30, 45 % 30) = gcd(30, 15)
    #gcd(30, 15) = gcd(15, 30 % 15) = gcd(15, 0) = 15

print(Gcd(10,4))