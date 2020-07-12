with open("for buddies.txt") as f:#"favoriteMovies.txt"
    content = f.readlines()
onelist=[]

for x in content:
    line = x.strip()
    sList=line.split(":")

    onelist.append(sList)
print(onelist)

def preChange_movie(alist,maxLength):
    var="@"
    for k in range(len(alist)):
        while len(alist[k]) < maxLength+1:#+1 in order to make all first is @, then we can put all leftdigt to the index 0 list
            alist[k] = var + alist[k]

def radix_sort_movie(alist):#it sort each small movie list in order to compare same set.

    new = alist[1].split(",")
    alist[1] = new
    alist1=alist[1]#alist1 ['x','zz','ss'] movie set.

    len_alist = len(alist1)
    index=-1
    maxLength=0
    for n in alist1:
        if len(n)>maxLength:
            maxLength=len(n)
    preChange_movie(alist1, maxLength)
    while True:
        counting_list = []
        for i in range(27):
            counting_list.append([])
        for str1 in alist1:  # b,x,b,n
            char = str1[index]
            var = char
            if char == " " or char == ",":
                var = "@"
            charNO = ord(var) - 64  # after compare all digit from right to left, now the charNO should be 0.
            counting_list[charNO].append(str1)
        index -= 1

        alist1 = []
        for x in counting_list:
            for y in x:
                alist1.append(y)
        newlist = []
        str=","

        for c in alist1:#delete all @ in front of the movie and add them to a newlist
            element=c.strip("@")
            newlist.append(element)
        combine=str.join(newlist)#[' ',' '...] to ['      ']
        outlist=[alist[0], combine]#['id','        ']
        if len(counting_list[0]) == len_alist:  # because when digt_now=0,all value add into counting_list[0],the length same ,
            # it means it has compared all digit from right to left
            return outlist

def preChange(alist,maxLength):
    var="@"
    for k in range(len(alist)):
        while len(alist[k][1]) < maxLength+1:#+1 in order to make all first is @, then we can put all leftdigt to the index 0 list
            alist[k][1] = var + alist[k][1]


def radix_sort(alist):
    #var=" "
    len_alist = len(alist)
    index=-1
    maxLength=0
    for i in range(len(alist)):
        if len(alist[i][1])>maxLength:
            maxLength=len(alist[i][1])

    #make all length be same by adding @in front of character
    preChange(alist,maxLength)

    while True:
        counting_list = []
        for i in range(27):
            counting_list.append([])

        for k in range(len(alist)):  # b,x,b,n
            char = alist[k][1][index]
            var = char
            if char == " " or char == ",":
                var = "@"
            charNO = ord(var) - 64  # after compare all digit from right to left, now the charNO should be 0.
            counting_list[charNO].append(alist[k])
        index -= 1
        alist = []
        for x in counting_list:

            for y in x:
                alist.append(y)

        newlist = []

        for c in alist:
            element=c[1].strip("@")
            newlist.append([c[0],element])

        if len(counting_list[0]) == len_alist:  # because when digt_now=0,all value add into counting_list[0],the length same ,
            # it means it has compared all digit from right to left
            return newlist

def getSame(sortedList):#put same movie to a sublist
    groupList = []
    subList = []
    for i in range(len(sortedList)):
        if i + 1 < len(sortedList):
            if sortedList[i][1] == sortedList[i + 1][1]:
                subList.append(sortedList[i])

            else:
                subList.append(sortedList[i])  # when 2,3 append 2, append until i+1 is different element

                if len(subList)>=2:
                    groupList.append(subList)  # append a list containing all same element to  a

                    subList = []
                else:
                    subList=[]
        else:
            subList.append(sortedList[len(sortedList)-1 ])  # append the last element to x

            if len(subList)>=2:

                groupList.append(subList)  # append [x] to a
    return groupList


a=[]
for subList in onelist:      #first radixsort every [id,move set],make each ovie set in order
    a.append(radix_sort_movie(subList))

sortedList=radix_sort(a)    #radix sort all sublist,then buddies who like same movie will be together

setList=getSame(sortedList) #put list of buddies who like same movie to same list
# print(setList)
for z in range(len(setList)):
    print("-------------------")
    print("GROUP",z+1)
    id = []
    for w in range(len(setList[z])):
        id.append(setList[z][w][0])
    #print(id) ['id','id2','id3'...]
    buddies=" ".join(id)  #id1 id2 id3 id4
    print("movies：",setList[z][1][1])
    print("Buddies:", buddies)
