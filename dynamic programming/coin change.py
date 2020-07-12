def coin_change(Coins,V):


    infinity=100000000000000000000000000000
    memo=[infinity for x  in range(V+1)]
    decision=[0 for x  in range(V+1)]
    N=len(Coins)
    memo[0]=0
    for v in range(1,V+1):
        minCoins=infinity
        for i in range(N):
            if Coins[i]<=v:
                c=1+memo[v-Coins[i]]
                if c<minCoins:
                    minCoins=c
                    coin=Coins[i]
        memo[v]=minCoins
        decision[v]=coin
    Solution = []
    while V != 0:
        Solution.append(decision[V])
        V = V-decision[V]

    print(memo)
    print("minimum coin numver:",memo[-1])
    # print(decision)
    # print(decision[-1])
    print("chosed coins:",Solution)
Coins = [9, 5, 6, 1]
V=int(input("please enter a value:"))
coin_change(Coins,V)


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










    # V = 20
    # coins = [9, 5, 6, 1]
    # N = len(coins)
    # Memo = [0] * 20
    #
    # # Memo[0]=0
    # for v in range(1, V):
    #     minCoins = 10000000000
    #     for i in range(N):
    #         if coins[i] <= v:
    #             c = 1 + Memo[v - coins[i]]
    #             if c < minCoins:
    #                 minCoins = c
    #     Memo[v] = minCoins
    #
    # print(Memo[13])