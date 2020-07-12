def counting_sort(a_list):
    max=a_list[0]
    for i in range(1,len(a_list)):
        if a_list[i]>max:
            max=a_list[i]
    max=max+1
    #create an empty list all 0
    count_list=[0]*max
    print(count_list)
    for value in a_list:
        count_list[value]+=1
    output_list=[]
    for x in range(len(count_list)):
        NumberOfOccurences=count_list[x]
        for w in range(NumberOfOccurences):
            output_list.append(x)
    print(output_list)
alist=[3,1,3,7,5,3,7,8]
counting_sort(alist)

