weight=[6,1,5,9]
value=[230,40,350,550]
n=len(value)
c=12


def knapsack(weight,value,n,c):
    memo=[[0 for x in range(c+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            case1=memo[i-1][j]
            if weight[i-1]<=j:
                case2=value[i-1]+memo[i-1][j-weight[i-1]]

print(knapsack(weight,value,n,c))















# def knapsack(weight,value,n,C):
#     Matrix=[[0 for x in range(C+1)]for x in range(n+1)]
#     print(Matrix)
#     for i in range(1,n+1):
#         for c in range(1,C+1):
#             case1=Matrix[i-1 ][c]
#             case2=0
#             if weight[i-1]<=c:
#                 case2 = value[i-1] + Matrix[i - 1][c - weight[i-1]]
#             Matrix[i][c]=max(case1,case2)
#             # else:
#             #     Matrix[i][c]=case1
#     return Matrix[n][C]












# weight=[4,3,1]
# value=[3000,2000,1000]
# n=len(value)
# w=4
# def knapsack(weight,value,n,w):
#     Matrix=[[0 for x in range(w+1)]for x in range(n+1)]
#     for i in range(1,n+1):
#         for j in range(1,w+1):
#             case1=Matrix[i-1][j]
#             case2=value[i-1]+Matrix[i-1][j-weight[i-1]]
#             if weight[i-1]<=w:
#                 Matrix[i][j]=max(case1,case2)
#             else:
#                 Matrix[i][j]=case1
#     return Matrix[n][w]
#
# print(knapsack(weight,value,n,w))