sequence=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,3, 11, 7, 15]

alist_of_list=[[0 for x in range(2)]for y in range(len(sequence)) ]
print(alist_of_list)
for i in range(len(sequence)):
    alist_of_list[i][0]=sequence[i]
    alist_of_list[i][1]=1

print(alist_of_list)
for j in range(len(alist_of_list)):
    for k in range(j-1,-1,-1):
        if alist_of_list[j][0]>alist_of_list[k][0]:
            if alist_of_list[j][1]<=alist_of_list[k][1]:
                alist_of_list[j][1]=alist_of_list[k][1]+1

print(alist_of_list)











