def Fibonacci(N):
    if N==1 or N==2:
        return 1
    else:
        return Fibonacci(N-1)+Fibonacci(N-2)#time complexity is exponential time

print(Fibonacci(0))