def binary(n,prev,out,index):
	if n==0:
		for j in range(len(out)):
			print(out[j],end=" ")
		print()
		return
	else:
		if prev==0 or prev==-1:
			out[index]=0
			binary(n-1,0,out,index+1)
			out[index]=1
			binary(n-1,1,out,index+1)
		else:
			out[index]=0
			binary(n-1,0,out,index+1)
		


def main():
	n=int(input())
	out=[-1]*n
	binary(n,-1,out,0)
if __name__=="__main__":
	main()