L=10
# l=[0,1,2,3,4,5,6,7,8,9,10]
p=[0,1,4,6,8,8,9,15,17,18,19]

def cut_ord(L,p):
    r=[0 for x in range(L+1)]
    for i in range(1,L+1):
        best=p[i]
        for j in range(1,i):
            this_value=p[j]+r[i-j]
            if this_value>best:
                best=this_value
        r[i]=best
    cuts=[]
    # i=L
    while L>0:
        best_cut=L
        best_value=p[L]
        for j in range(1,L):
            value=p[j]+r[L-j]
            if value>best_value:
                best_cut=j
                best_value=value
        cuts.append(best_cut)
        L-=best_cut
    return r[-1],cuts


print(cut_ord(L,p))#(4,17)





































#
# def cut_rod_memo(L,p,cut_memo):
#     if L==0:
#         return 0
#     elif cut_memo[L] !=-1:
#         return cut_memo[L]
#     else:
#         best=p[L]
#         for i in range (1,L+1):
#             best=max(best,cut_rod_memo((L-i),p,cut_memo))
#         cut_memo[L]=best
#         print(cut_memo[L])
#         return best
#
# def cut_rod(L,P):
#     cut_memo=[-1 for x in range(L+1) ]
#     cut_memo[0]=0
#     return cut_rod_memo(L,p,cut_memo)
# print(cut_rod(L,p))

