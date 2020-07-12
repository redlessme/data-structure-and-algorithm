#Write a program to print all prime numbers between 1 and N.

def prime(N):
    for i in range(1,N+1):
        f=True
        for j in range(2,i):# cannot divide by number except 1 and itself

            if i%j==0:
                f=False
                break
        if f==True:
            print(i)
prime(100)