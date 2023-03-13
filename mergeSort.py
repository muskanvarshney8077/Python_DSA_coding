from sys import setrecursionlimit
setrecursionlimit (1000000000)

# def merge(arr,l,mid,r):
#     n=mid-l+1
#     m=r-mid
#     arr1=[0]*n 
#     arr2=[0]*m 
#     for i in range(n):
#         arr1[i]=arr[l+i]
#     for j in range(m):
#         arr2[j]=arr[mid+1+j]
#     i=0
#     j=0
#     k=l 
#     arr3=[]
#     while(i<n and j<m):
#         if arr1[i]<arr2[j]:
#             arr3[k]=arr1[i]
#             k+=1
#             i+=1 
#         else:
#             arr3[k]=arr2[j]
#             k+=1
#             j+=1
#     while(i<n):
#         arr3[k]=arr1[i]
#         i+=1
#         k+=1
#     while(j<m):
#         arr3[k]=arr2[j]
#         j+=1
#         k+=1
#     print(arr3)

def merge(arr,l,mid,r):
    n=mid-l+1
    m=r-mid
    arr1=[0]*n 
    arr2=[0]*m 
    for i in range(n):
        arr1[i]=arr[l+i]
    for j in range(m):
        arr2[j]=arr[mid+1+j]
    i=0
    j=0
    k=l
    arr3=[]
    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
    
            i+=1
    
            k+=1

        else:
            arr3[k]=arr2[j]
            j+=1
            k+=1
    while(i<n):
        arr3[k]=arr1[i]
        k+=1
        i+=1
    while(j<m):
        arr3[k]=arr2[j]
        j+=1
        k+=1
    print(arr3)



def mergeSort(arr,l,r):
    if l<r:
        mid=l+(r-l)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)

def main():   
    arr=[int(x) for x in input().split()]
    mergeSort(arr,0,len(arr)-1)
if __name__=="__main__":
    main()
    