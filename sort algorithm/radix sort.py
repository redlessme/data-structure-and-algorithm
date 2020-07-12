def radix_sort(alist):

    len_alist = len(alist)
    mod = 1
    while True:
        counting_list = []
        for i in range(10):
            counting_list.append([])
        #print(counting_list)
        for value in alist:
            digit_now = int((value /mod)%10)   #after compare all digit from right to left, now the digit_now should be 0.
            counting_list[digit_now].append(value)
        mod = mod * 10
        #print("clist",counting_list)

        if len(counting_list[0]) == len_alist:  #because when digt_now=0,all value add into counting_list[0],the length same ,
            #it means it has compared all digit from right to left
            return counting_list[0]
        alist = []
        for x in counting_list:
            for y in x:
                alist.append((y))
        #print("alist", alist)

alist = [119, 223, 114, 103, 200, 110, 332, 3321,11911]

print("output",radix_sort(alist))



