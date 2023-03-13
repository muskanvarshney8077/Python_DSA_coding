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
		if self.head == None:
			self.head=newNode
			self.tail=newNode
		else:
			self.tail.next=newNode
			self.tail=newNode
	def printf(self):
		temp=self.head
		while(temp is not None):
			print(temp.data,end=" ")
			temp=temp.next
	def mid(self,start,last):
		if start ==None:
			return None
		slow=start
		fast=start.next
		while(fast != last):
			fast=fast.next
			if fast!=last:
				fast=fast.next
				slow=slow.next
		return slow
	def binary(self,value):
		start=self.head
		last=None
		
		while(True):
			midi=self.mid(start,last)
			if midi==None:
				return None
			elif midi.data==value:
				return midi
			elif midi.data<value:
				start=midi.next
			else:
				last=midi
			if not(last==None or last!=start):
				break
		return None
			
def main():
	l=linked()
	l.insert(1)
	l.insert(2)
	l.insert(3)
	l.insert(4)
	l.printf()
	print()
	if l.binary(5)==None:
		print("not found")
	else:
		print("found")
if __name__=="__main__":
	main()

