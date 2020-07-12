value=[550,350,180,40]
weight=[9,5,6,1]
item=["A",'B','C','D']
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

    solution=[]
    while capacity>0:

        # for the_weight in weight:
        for i in range(N):
            if weight[i]<=capacity:
                if memo[capacity]==value[i]+memo[capacity-weight[i]]:
                    chosen_weight=weight[i]
                    chose_item=item[i]
        solution.append(chose_item)
        capacity=capacity-chosen_weight
    print(memo)
    print("max value can take:",memo[-1])
    print("solution:",solution)
unbounded_knapsack(value,weight,capacity)
