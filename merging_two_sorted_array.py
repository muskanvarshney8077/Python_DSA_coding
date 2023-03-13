arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
i=0
j=0
k=0
arr3=[0]*(len(arr1)+len(arr2))
while(i<len(arr1) and j<len(arr2)):
    if arr1[i]<arr2[j]:
        arr3[k]=arr1[i]
        i+=1
        k+=1
    else:
        
        arr3[k]=arr2[j]
        j+=1
        k+=1
while(i<len(arr1)):
    arr3[k]=arr1[i]
    k+=1
    i+=1
while(j<len(arr2)):
    arr3[k]=arr2[j]
    j+=1
    k+=1
print(arr3)


