# def binarySearch(alist,key): #must be sorted
#     lo=0
#     hi=len(alist)
#     while lo<hi-1:
#         mid = (lo+hi)//2
#         if key>=alist[mid]:
#             lo=mid
#         else:
#             hi=mid
#     if alist[lo]==key:
#         return "key found in position lo."
#     else:
#         return "key not found."
#
# alist=[1,4,7,100,100,450,20000,1000000]
# print(binarySearch(alist,100))

# def binary_search(alist,key):
#     lo=0
#     hi=len(alist)-1
#     while lo<=hi:
#         mid=(lo+hi)//2
#         if alist[mid]==key:
#             return mid
#         elif alist[mid]>key:
#             hi=mid-1
#         else:
#             lo=mid+1
#     return -1

def binary_search(alist,key):
    lo=0
    hi=len(alist)
    while lo<hi-1:
        mid=(lo+hi)//2
        if key>=alist[mid]:
            lo=mid
        else:
            hi=mid

    if len(alist)>0 and alist[lo]==key:
        return True
    else:
        return False


alist=[1,4,7,100,100,450,20000,1000000]
print(binary_search(alist,100))