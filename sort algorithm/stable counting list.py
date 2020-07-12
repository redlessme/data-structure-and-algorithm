def counting_sort(a_list):
    max = a_list[0]
    for i in range(1, len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
    max = max+1
    print(max)

    counting_list = []  # create an list of list all [[],[]...]
    for i in range(max):
        counting_list.append([])
    print(counting_list)
    for value in a_list:
        geWei=value%10
        counting_list[geWei].append(value)
    print("个位",counting_list)
    output_list = []
    for x in range(len(counting_list)):
        numberOfOccurences = len(counting_list[x])
        for w in range(numberOfOccurences):
            output_list.append(x)
    print(output_list)





alist = [90, 32, 44, 31,10, 10, 22, 25, 12]
# counting_sort(alist)
counting_sort(alist)


