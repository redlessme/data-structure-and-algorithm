# length=[1,2,3,4,5,6,7,8,9,10]
# value=[1,4,6,8,8,9,15,17,18,19]
value=[2,5,7,8]
n=len(value)
L=5
def knapsack(value,n,L):
    Matrix=[[0 for x in range(L+1)]for y in range(n+1)]
    for i in range(1,n+1):
        for c in range(1,L+1):
            case1=Matrix[i-1 ][c]
            case2=0
            if i<=c:
                case2 = value[i-1] + Matrix[i][c -i]
            Matrix[i][c]=max(case1,case2)
        # else:
        #     Matrix[i][c]=case1
    return Matrix[n][L]

print(knapsack(value,n,L))