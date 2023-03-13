def partition(arr,low,high):
	i=low-1
	
	for j in range(low,high):
		if arr[j]<=arr[high]:
			i=i+1
			arr[j],arr[i]=arr[i],arr[j]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return i+1
def quickSort(arr,low,high):
	if low<high:
		p=partition(arr,low,high)
		quickSort(arr,low,p-1)
		quickSort(arr,p+1,high)
def main():
	arr=[]
	for ele in input().split():
		arr.append(int(ele))
	print("before sorting")
	print(arr)
	print("after sorting")
	quickSort(arr,0,len(arr)-1)
	print(arr)
if __name__=="__main__":
	main()


