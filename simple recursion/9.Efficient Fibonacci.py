def FibonacciIter(N):  # when n is big ,iteration is more effient than recursion.
    n1=1
    n2=1
    n3=1
    if N<1:
        print("Wrong input!")
        return -1
    else:
        while N>2:
            n3=n1+n2
            n1=n2
            n2=n3
            N-=1
        return n3
number=int(input("Please enter a number"))

if FibonacciIter(number)!=-1:
    print(FibonacciIter(number)) #Fi:1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, . . .

