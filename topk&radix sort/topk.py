with open("for top.txt") as f:#"timeSpent.txt"
    content = f.readlines()
alist=[]
for x in content:
    line=x.strip()
    sList=line.split(":" )
    sList[0],sList[1] = int(sList[0]),int(sList[1])
    alist.append(sList)

def buildMinHeap(array): #build a min heap
    length=len(array)-1
    for i in range(length//2,-1,-1):
        heapify(array,i,length)

def heapSort(array): #build a min heap
    buildMinHeap(array)   #o(k)
    length=len(array)-1
    for j in range(length,0,-1): #olog(k)
        swap(array,0,j)
        heapify(array,0,j-1)#j-1 means ignore the last(max) element

def swap(A, x, y):
    A[x],A[y]=A[y],A[x]

def heapify(array,low,high): #min_heap heapify, keep it is a min heap
    i=low
    j=2*low+1 #it is left child,because index from 0 in the list
    while j<=high:
        if j <high and array[j][1]>array[j+1][1]:#find min child
            j+=1
        elif j<high and array[j][1]==alist[j+1][1]:
            if array[j][0]>array[j+1][0]:
                j+=1
        if array[i][1]>array[j][1]: #swap parent and min child
            swap(array,j,i)
            i = j
            j = 2 * i+1

        elif array[i][1] == array[j][1] and array[j][0]>array[i][0]:
            swap(array, j, i)
            i = j
            j = 2 * i + 1
        else:
            return

def findMaxKInN(alist, K):
    N=len(alist)
    heapList = []
    for i in range(K):
        heapList.append(alist[i])
    buildMinHeap(heapList)

    for i in range(K,N):#compare k+1 to N elements in alist with the min element in the heap list
        if heapList[0][1] < alist[i][1]:
            heapList[0] = alist[i]
            heapify(heapList, 0,len(heapList)-1)#keep the heaplist is a min heap

        elif heapList[0][1]==alist[i][1] and heapList[0][0]>alist[i][0]:#if same time and alist's element id smaller,replace the min element
            heapList[0] = alist[i]
            heapify(heapList, 0,len(heapList)-1)#keep the heaplist is a min heap

    heapSort(heapList)

    for w in range(len(heapList) ):
        print("#", w+1 , ": User ID:", heapList[w][0], "time spent:", heapList[w][1])

k=int(input("please enter a number:"))
findMaxKInN(alist,k)