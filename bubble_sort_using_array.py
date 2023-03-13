arr=[int(x) for x in input().split()]
print("before bubble sorting")
print(arr)
for i in range(len(arr),-1,-1):
    for j in range(i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("after sorting")
print(arr)
        
