sequence=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
alist=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for i in range(0,len(sequence)):
    alist[i][0]=sequence[i]
    alist[i][1]=1
maximum=0
for j in range(1,len(alist)):
    for k in range(j-1,-1,-1):
        if alist[j][0] > alist[k][0]:
            if alist[j][1] <= alist[k][1]:
                alist[j][1] = alist[k][1] + 1
        # if alist[j][1] > maximum:
        #     maximum = alist[j][1]

print(alist)