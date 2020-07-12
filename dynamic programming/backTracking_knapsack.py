weight=[6,1,5,9]
value=[230,40,350,550]
item=["A","B","C","D"]
n=len(value)
c=12
def knapsack(weight,value,n,C):
    Matrix=[[0 for x in range(C+1)]for x in range(n+1)]
    decision = [0 for x in range(C + 1)]
    for i in range(1,n+1):
        for c in range(1,C+1):
            case1=Matrix[i-1 ][c]
            case2=0
            if weight[i-1]<=c:
                case2 = value[i-1] + Matrix[i - 1][c - weight[i-1]]
                the_item=item[i-1]
            Matrix[i][c]=max(case1,case2)
            decision[c]=the_item
            Solution = []
            while C != 0:
                Solution.append(decision[C])
                C = C - decision[C]
    print(Solution)

    print(Matrix[n][C])

    # solution=[]
    # while capacity>0:
    #
    #     # for the_weight in weight:
    #     for i in range(N):
    #         if weight[i]<=capacity:
    #             if memo[capacity]==value[i]+memo[capacity-weight[i]]:
    #                 chosen_weight=weight[i]
    #                 chose_item=item[i]
    #     solution.append(chose_item)
    #     capacity=capacity-chosen_weight
    # print(memo)


    # solution=[]
    # while C>0:
    #
    #     # for the_weight in weight:
    #     for k in range(n,0,-1):
    #         # print(k,"k")
    #         # print(weight[k-1])
    #         # print(C)
    #         if weight[k-1]<=C:
    #             # print(value[k-1],"value[k-1]")
    #             # print(Matrix[k-1][C-weight[k-1]])
    #             if Matrix[k][C]==max(value[k-1]+Matrix[k-1][C-weight[k-1]],Matrix[k-1][C]):
    #
    #                 # print(Matrix[k][C],"a")
    #                 # print(value[k-1])
    #                 # print(Matrix[k-1][C-weight[k-1]])
    #                 chosen_weight=weight[k-1]
    #                 chose_value=value[k-1]
    #
    #                 #print("c",chose_value)
    #                 break
    #                 # print("chosen:",chose_value)
    #     solution.append(chose_value)
    #     C=C-chosen_weight
    #
    #
    # print("solution:",solution)

knapsack(weight,value,n,c)


