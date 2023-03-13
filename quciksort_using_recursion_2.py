def quick(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
    return quick(less)+[pivot]+quick(greater)
def main():
    arr=[]
    for ele in input().split():
        arr.append(int(ele))
    arr=quick(arr)
    print(arr)
    
if __name__=="__main__":
    main()