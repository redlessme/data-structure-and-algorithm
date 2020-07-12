# def insertionSort(alist):
#     for i in range(1,len(alist)):
#         j=i
#         while j>=0 and alist[j]<alist[j-1]:
#             alist[j-1],alist[j]=alist[j],alist[j-1]
#             j-=1




def insertionSort(alist):
    for i in range(1,len(alist)):
        j=i
        while alist[j-1]>alist[j] and j>0:
            alist[j-1],alist[j]=alist[j],alist[j-1]
            j-=1
alist=[-3.9,-1,38,7,6,99]
insertionSort(alist)
print(alist)
