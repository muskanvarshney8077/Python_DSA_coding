def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
import sys
sys.setrecursionlimit(11000)
def main():
	n=int(input())
	print(fact(n))
if __name__=="__main__":
	main()