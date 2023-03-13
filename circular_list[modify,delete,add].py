class node:
  def __init__(self,data):
    self.data=data
    self.next=None 
class circular:
  def __init__(self):
    self.head=None
    self.tail=None
  def atBeg(self,data):
    newNode=node(data)
    if self.head == None:
      self.head=newNode
      self.tail=newNode
      
    else:
      newNode.next=self.head
      self.head=newNode
      self.tail.next=self.head
  def atEnd(self,data):
    newNode=node(data)
    if self.head ==None:
      self.head=newNode
      self.tail=newNode
    else:
      self.tail.next=newNode
      self.tail=newNode
      newNode.next=self.head
  def printf(self):
    temp=self.head
    while(temp is not self.tail):
      print(temp.data,end=" ")
      temp=temp.next
    print(self.tail.data)
  def count(self):
    temp=self.head
    if self.head is None:
      count=0
    else:
      count=1
    while(temp is not self.tail):
      count=count+1
      temp=temp.next 
    return count

  def atPos(self,data,n):
    newNode=node(data)
    i=self.count()
    if n==0:
      self.atBeg()
    elif n>i:
      self.atEnd()
    else:
      temp=self.head
      for i in range(n-1):
        prev=temp
        temp=temp.next 
      newNode.next=temp
      prev.next=newNode
  def atBegDel(self):
    temp=self.head 
    self.head=self.head.next
    self.tail.next=self.head
    temp.next=None
  def atEndDel(self):
    temp=self.head
    while(temp.next is not self.tail):
      temp=temp.next
    self.tail=None
    self.tail=temp
    self.tail.next=self.head
  def atPosDel(self,n):
    i=self.count()
    if n==0:
      self.atBegDel()
    elif n>i:
      self.atEndDel()
    else:
      temp=self.head 
      for i in range(n-1):
        prev=temp 
        temp=temp.next 
      prev.next=temp.next
      temp.next=None


      
def main():
  c=circular() 
  print("addition in beginning")
  c.atBeg(1)
  c.atBeg(2)
  c.atBeg(3)
  c.printf()
  print("addition at end")
  c.atEnd(4)  
  c.printf()
  print("count of list")
  print(c.count())
  print("addition on specific area like at position 2")
  c.atPos(5,2)
  c.printf()
  print("delete from front")
  c.atBegDel()
  c.printf()
  print("delete from end")
  c.atEndDel()
  c.printf()
  print("delete from second position")
  c.atPosDel(2)
  c.printf()
if __name__=="__main__":
  main()  