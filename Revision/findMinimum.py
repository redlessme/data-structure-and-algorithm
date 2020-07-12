arr=[2,-1,9,0,8]
min=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
print(min)