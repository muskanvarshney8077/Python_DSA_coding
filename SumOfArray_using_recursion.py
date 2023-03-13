def sum(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+sum(arr[1::])
def main():
    arr=[]
    for ele in input().split():
        arr.append(int(ele))
    print(sum(arr))
if __name__=="__main__":
    main()

