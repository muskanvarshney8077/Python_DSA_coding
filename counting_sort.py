#counting sort
def countSort(arr,n,k):
    
    freq=[0]*(k+1)
    for i in range(n):
        freq[arr[i]]+=1
    count=[0]*(k+1)
    count[0]=freq[0]
    for j in range(1,k):
        count[j]=count[j-1]+freq[j]
    
    brr=[0]*n
    for i in range(n-1,-1,-1):
        count[arr[i]]-=1
        brr[count[arr[i]]]=arr[i]

    return brr



def main():
    arr=[int(x) for x in input().split()]
    print(countSort(arr,len(arr),max(arr)))

if __name__=="__main__":
    main()