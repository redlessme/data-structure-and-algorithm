def counting_sort(a_list):
    max=26+1

    #create an empty list all 0
    count_list=[0]*max
    print(count_list)
    for char in a_list:
        count_list[ord(char)-64]+=1
    output_list=[]
    for x in range(len(count_list)):
        NumberOfOccurences=count_list[x]
        for w in range(NumberOfOccurences):
            output_list.append(chr(x+64))
    print(output_list)
alist=["B","C","D","B","C","A"]
counting_sort(alist)

