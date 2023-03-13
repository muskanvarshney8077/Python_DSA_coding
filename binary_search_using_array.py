import sys
sys.setrecursionlimit(10000000)
def binary(arr,low,high,find):
	if high>=low:
		midi=low+(high-low)//2
	
		if arr[midi]==find:
			return midi
		elif arr[midi]<find:
			return binary(arr,midi+1,high,find)
		else:
			return binary(arr,low,midi-1,find)
	else:
		
		return -1
def main():
	arr=[]
	for ele in input().split():
		arr.append(int(ele))
	print(arr)
	print("what to find")
	find=int(input())
	index=binary(arr,0,len(arr)-1,find)
	print(index)
	if index!=-1:
		print("found")
	else:
		print("Not found")
if __name__=="__main__":
	main()
	