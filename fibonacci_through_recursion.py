def fibo(n):
	if n==1 or n==0:
		return n
	return fibo(n-1)+fibo(n-2)
import sys
sys.setrecursionlimit(11000)
def main():
	n=int(input())
	print(fibo(n))
if __name__=="__main__":
	main()
