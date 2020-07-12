# def selectionSort(alist):
#     for i in range (0,len(alist)-1):
#         min_index=i
#         for j in range(i+1,len(alist)):
#             if alist[j]<alist[min_index]:
#                 min_index=j
#         alist[i],alist[min_index]=alist[min_index],alist[i]
#
#
#
#
# def selectionSort(alist):
#     for i in range(0,len(alist)-1):
#         min_index=i
#         for j in range(i+1,len(alist)):
#             if alist[j]<alist[min_index]:
#                 min_index=j
#         alist[i],alist[min_index]=alist[min_index],alist[i]



def selectionSort(alist):
    for i in range(0,len(alist)-1):
        min_index=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[min_index]:
                min_index=j
        alist[i],alist[min_index]=alist[min_index],alist[i]

alist=[5,-2,7,1,10,9]
selectionSort(alist)
print(alist)
