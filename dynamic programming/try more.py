weight=[6,1,5,9]
value=[230,40,350,550]
n=len(value)
c=12
def knapsack(weight,value,n,C):
    Matrix=[[0 for x in range(C+1)]for x in range(n+1)]
    # print(Matrix)
    for i in range(1,n+1):
        for c in range(1,C+1):
            case1=Matrix[i-1 ][c]
            case2=0
            if weight[i-1]<=c:
                case2 = value[i-1] + Matrix[i - 1][c - weight[i-1]]
            Matrix[i][c]=max(case1,case2)
            # else:
            #     Matrix[i][c]=case1
    print(Matrix[n][C])
    # print(Matrix)
    #
    # decision=[False for x in range(n+1)]
    # print(decision)
    #
    # for k in range(1,n+1):
    #     if Matrix[k][C]>Matrix[k-1][C]:
    #         decision[k-1]=True
    #         print(decision[k-1])
    #         C=C-weight[k-1]
    #         print(decision)
    # for y in range(1,n):
    #     if decision[y]:
    #         print("the"+str(y)+"th")

knapsack(weight,value,n,c)