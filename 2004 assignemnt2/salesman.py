def salesman(N, price, k):
    memo=[0 for x in range(N+1)]

    for i in range(1,N+1):
        the_value= price[i - 1] + memo[i - k - 1]

        memo[i]=max(the_value,memo[i-1])
    print(memo)
    # backtracking
    solution=[]
    while N>0:
        if memo[N] !=memo[N-1]:
                solution.append(N)
                N=N-(k+1)
        else:
            N=N-1
    solution.reverse()
    sum="Houses:"
    for house in solution:
        sum+=(str(house)+" ")
    print(sum)
    print("Total Sale:",memo[-1])
with open("houses.txt") as f:
    content = f.readlines()
    alist=[]
    blist=[]
    price=[]
    for x in content:
        line=x.strip()
        alist.append(line)
    blist.append(alist[1])
    for y in blist:
        num=str(y).split()
    for str1 in num:
        price.append(int(str1))
    N=len(price)

k=int(input("Enter value of k:"))
assert 0<k<=N,"k must  be a positive integer smaller than or equal to N!"
salesman(N, price, k)