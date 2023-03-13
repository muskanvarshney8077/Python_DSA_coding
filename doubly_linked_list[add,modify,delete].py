class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class doublyLinked:
  def __init__(self):
    self.head=None
    self.tail=None
  def printf(self):
    temp=self.head 
    while(temp is not None):
      print(temp.data,end=" ")
      temp=temp.next
  def leftRotate(self,n):
    temp=self.head
    for i in range(n):
      prev_node=temp
      temp=temp.next
    prev_node.next=None
    temp.prev=None
    self.tail.next=self.head
    self.head.prev=self.tail
    self.head=temp 


  def atBed(self,data):
    newNode=Node(data)
    if self.head==None:
      self.head=newNode
      self.tail=newNode
    else:
      self.head.prev=newNode
      newNode.next=self.head
      self.head=newNode
  def printfRev(self):
    temp=self.tail
    while(temp is not self.head):
      print(temp.data,end=" ")
      temp=temp.prev
    print(temp.data)
    
    
    
  def atEnd(self,data):
    newNode=Node(data)
    if self.head==None:
      self.head=newNode
      self.tail=newNode
    else:
      self.tail.next=newNode
      newNode.prev=self.tail
      self.tail=newNode
  def count(self):
    temp=self.head
    count=0
    while(temp is not None):
      count=count+1
      temp=temp.next
    return count

  def atPos(self,data,n):
    newNode=Node(data)
    if n==1:
      self.atBed()
    elif n>self.count():
      self.atEnd()
    else:
      temp=self.head
      for i in range(n-1):
        temp=temp.next
      newNode.prev=temp
      newNode.next=temp.next
      temp.next.prev=newNode
      temp.next=newNode
  def atBegDel(self):
    if self.head.next is None:
      self.head=None
      return
    temp=self.head.next
    self.head.next=None
    temp.prev=None
    self.head=temp
  def atEndDel(self):
    if self.head.next is None:
      self.head=None
      return
    temp=self.tail.prev
    self.tail.prev=None
    temp.next=None
    self.tail=temp 
  def atPosDel(self,i):
    n=self.count()
    if  i==1:
      self.atBegDel()
    elif i==n-1:
      self.atEndDel()
    else:
      temp=self.head
      for i in range(i-1):
        prev_node=temp
        temp=temp.next
      prev_node.next=temp.next
      temp.next.prev=prev_node 
      temp.next=None
      temp.prev=None

def main():
  d=doublyLinked()
  d.atBed(1)
  d.atBed(2)
  d.atBed(3)
  d.printf()
  print()
  d.atEnd(4)
  d.printf()
  print()
  d.atPos(45,3)
  d.printf()
  print()
  d.atBegDel()
  d.printf()
  print()
  d.atEndDel()
  d.printf()
  print()
  d.atBed(12)
  d.atBed(9)
  print()
  d.printf()
  print()
  d.atPosDel(2)
  d.printf()
  print("rotate left by 3")
  d.leftRotate(3)
  d.printf()
 
 

if __name__=="__main__":
  main()