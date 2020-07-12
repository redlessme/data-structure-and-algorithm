# # 如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元
#
#
# def select_coin(coin_value, total_value):
#     min_coin_num = [0]
#     for i in range(1, total_value + 1):
#       min_coin_num.append(float('inf'))
#       for value in coin_value:
#          if value <= i and min_coin_num[i - value] + 1 < min_coin_num[i]:
#              min_coin_num[i] = min_coin_num[i - value] + 1
#
#     return min_coin_num
#
#
# result = select_coin([1, 3, 5], 11)
# print(result)
# print("coin number:" + str(result[-1]))
#
#
# weight=[6,1,5,9]
# value=[230,40,350,550]
# n=len(value)
# c=12
# def knapsack(weight,value,n,C):
#     Matrix=[[0 for x in range(C+1)]for x in range(n+1)]
#     print(Matrix)
#     for i in range(1,n+1):
#         for c in range(1,C+1):
#             case1=Matrix[i-1][c]
#             case2=0
#             if weight[i-1]<=c:
#                 case2 = value[i-1] + Matrix[i - 1][c - weight[i-1]]
#             Matrix[i][c]=max(case1,case2)
#             # else:
#             #     Matrix[i][c]=case1
#     return Matrix[n][C]
#
# print(knapsack(weight,value,n,c))

# def bag(n,c,w,v):
# 	res=[[-1 for j in range(c+1)] for i in range(n+1)]
# 	for j in range(c+1):
# 		res[0][j]=0
# 	for i in range(1,n+1):
# 		for j in range(1,c+1):
# 			res[i][j]=res[i-1][j]
# 			if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
# 				res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
# 	return res

def bag(n,c,w,v):
	res=[[-1 for j in range(c+1)] for i in range(n+1)]
	for j in range(c+1):
		res[0][j]=0
	for i in range(1,n+1):
		for j in range(1,c+1):
			res[i][j]=res[i-1][j]
			if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
				res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
	return res

def show(n,c,w,res):
	print('最大价值为:',res[n][c])
	x=[False for i in range(n)]
	j=c
	for i in range(1,n+1):
		if res[i][j]>res[i-1][j]:
			x[i-1]=True
			j-=w[i-1]
	print('选择的物品为:')
	for i in range(n):
		if x[i]:
			print('第',i,'个,',end='')
	print('')

if __name__=='__main__':
	n=5
	c=10
	w=[2,2,6,5,4]
	v=[6,3,5,4,6]
	res=bag(n,c,w,v)
	show(n,c,w,res)