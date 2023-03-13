#linked list
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linked:
	def __init__(self):
		self.head=None
		self.tail=None
	def count(self):
		temp=self.head
		count=0
		while(temp is not None):
			temp=temp.next
			count+=1
		return count
		
			
	
	def AtEnd(self,data):
		newNode=Node(data)
		if self.head==None:
			self.head=newNode
			self.tail=newNode
		else:
			self.tail.next=newNode
			self.tail=newNode
	def AtBeg(self,data):
		newNode=Node(data)
		if self.head ==None:
			self.head=newNode
			self.tail=newNode
		else:
			
			newNode.next=self.head
			self.head=newNode
	def AtPos(self,data,n):
		newNode=Node(data)
		if self.head is None:
			self.head=None
			self.tail=None
		elif n==1:
			self.AtBeg(data)
		elif n>self.count():
			self.AtEnd(data)
		else:
			temp=self.head
			for i in range(n-1):
				prev=temp
				temp=temp.next
			prev.next=newNode
			newNode.next=temp
	def atBegDel(self):
		temp=self.head
		self.head=self.head.next
		temp.next=None
	def atEndDel(self):
		temp=self.head
		while(temp.next.next is not None):
			temp=temp.next
		temp.next=None
	def delAtPos(self,n):
		temp=self.head
		if n==1:
			self.atBegDel()
		elif n==self.count():
			self.atEndDel()
		else:
			for i in range(n-1):
				prev=temp
				temp=temp.next
			prev.next=temp.next
			temp.next=None 


	def printf(self):
		temp=self.head
		while(temp is not None):
			print(temp.data,end=" ")
			temp=temp.next
def main():
	l=linked()
	l.AtEnd(1)
	l.AtEnd(2)
	l.AtEnd(3)
	l.printf()
	print()
	l.AtBeg(0)
	l.printf()
	print()
	l.AtPos(12,5)
	l.printf()
	print()
	l.atBegDel()
	l.printf()
	print()
	l.atEndDel()
	l.printf()
	print()
	l.delAtPos(3)
	l.printf()

if __name__=="__main__":
	main()