#Find middle of linked list
class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linked:
	def __init__(self):
		self.head=None
		self.tail=None
	def insert(self,data):
		newNode=node(data)
		if self.head==None:
			self.head=newNode
			self.tail=newNode
		else:
			self.tail.next=newNode
			self.tail=newNode
	def FindMid(self):
		slow=self.head
		fast=self.head.next
		while(fast is not None):
			slow=slow.next
			fast=fast.next.next
		print(slow.data)
	def printf(self):
		temp=self.head
		while(temp is not None):
			print(temp.data,end=" ")
			temp=temp.next

def main():
	l=linked()
	for ele in input().split():
		l.insert(ele)
	l.printf()
	print("middle element")
	l.FindMid()
if __name__=="__main__":
	main()