#
# memo=[0]*10
# memo[0]=0
# memo[1]=1
# for i in range(2,10):
#     memo[i]=-1
#
# def fibDP(N):
#     if memo[N] !=-1:
#         return memo[N]
#     else:
#         memo[N]= fibDP(N-1)+fibDP(N-2)
#         return memo[N]
#
# print(fibDP(8))
#

#bottom up  O(N)
memo=[0]*10
memo[0]=0
memo[1]=1
for i in range(2,len(memo)):
    memo[i]=memo[i-1]+memo[i-2]
print(memo)


memo=[0]*10
memo[0]=0
memo[1]=1
for i in range(2,len(memo)):
    memo[i]=-1
def fib(N):
    if memo[N]!=-1:
        return memo[N]
    else:
        memo[N]=fib(N-1)+fib(N-2)
        return memo[N]

print(fib(7))