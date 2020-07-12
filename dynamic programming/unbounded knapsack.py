# def coin_change(Coins,V):
#
#
#     infinity=100000000
#     memo=[infinity for x  in range(V+1)]
#     N=len(Coins)
#     memo[0]=0
#     for v in range(1,V+1):
#         minCoins=infinity
#         for i in range(N):
#             if Coins[i]<=v:
#                 c=1+memo[v-Coins[i]]
#                 if c<minCoins:
#                     minCoins=c
#         memo[v]=minCoins
#     print(memo)
#     print("minimum coin numver:",memo[-1])
# Coins = [9, 5, 6, 1]
# V=int(input("please enter a value:"))
# coin_change(Coins,V)


value=[550,350,180,40]
weight=[9,5,6,1]
capacity=int(input("please enter a value:"))#=12
def unbounded_knapsack(value,weight,capacity):
    memo=[0 for x in range(capacity+1)]
    N=len(weight)
    maxValue=0
    for c in range(1,capacity+1):
        for i in range(N):
            if weight[i]<=c:
                this_value=value[i]+memo[c-weight[i]]
                if this_value>maxValue:
                    maxValue=this_value
        memo[c]=maxValue
    print(memo)
    print("max value can take:",memo[-1])
unbounded_knapsack(value,weight,capacity)
