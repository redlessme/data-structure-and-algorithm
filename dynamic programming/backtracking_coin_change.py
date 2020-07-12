def coin_change(Coins,V):


    infinity=100000000
    memo=[infinity for x  in range(V+1)]
    N=len(Coins)
    memo[0]=0
    for v in range(1,V+1):
        minCoins=infinity
        for i in range(N):
            if Coins[i]<=v:
                c=1+memo[v-Coins[i]]
                if c<minCoins:
                    minCoins=c
        memo[v]=minCoins
    Solution = []
    while V > 0:
        for coin_value in Coins:
            if coin_value <= V:
                if memo[V] == 1 + memo[V - coin_value]:
                    chosen_coin = coin_value

        Solution.append(chosen_coin)
        V = V - chosen_coin
    print("memo:",memo)
    print("minimum coin numver:",memo[-1])
    print("solution:",Solution)

Coins = [9, 5, 6, 1]
V=int(input("please enter a value:"))
coin_change(Coins,V)