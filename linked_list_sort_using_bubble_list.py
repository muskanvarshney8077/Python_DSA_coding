class node:
  def __init__(self,data):
    self.data=data
    self.next=None 
class linkedList:
  def __init__(self):
    self.head=None
  def insert(self,data):
    newNode=node(data)
    if self.head==None:
      self.head=newNode
    else:
      newNode.next=self.head
      self.head=newNode
  def printf(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      temp=temp.next
  def sort(self):
    end=None
    while(end!=self.head.next):
      temp=self.head
      while(temp.next is not end):
        if temp.data<temp.next.data:
          temp.data,temp.next.data=temp.next.data,temp.data
        temp=temp.next
      end=temp
      
def main():
  l=linkedList()
  l.insert(6)
  l.insert(2)
  l.insert(3)
  l.insert(5)
  l.insert(1)

  l.printf()
  print("sorted")
  l.sort()
  l.printf()
if __name__=="__main__":
  main()