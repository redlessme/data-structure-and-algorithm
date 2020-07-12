# def selectionSort(alist):
#
#     for fillslot in range(len(alist)-1,0,-1):
#        positionOfMax=0
#        for location in range(1,fillslot+1):
#            if alist[location]>alist[positionOfMax]:
#                positionOfMax = location
#
#        temp = alist[fillslot]
#        alist[fillslot] = alist[positionOfMax]
#        alist[positionOfMax] = temp
#
#
#
def insertionSort(alist):

    for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist=['B','B','A','B','C','A']
insertionSort(alist)
print(alist)


