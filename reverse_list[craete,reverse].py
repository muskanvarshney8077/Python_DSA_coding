class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class reverse:
  def __init__(self):
    self.head=None
    self.tail=None
  def atBeg(self,data):
    newNode=node(data)
    if self.head==None:
      self.head=newNode
      self.tail=newNode
    else:
      newNode.next=self.head 
      self.head=newNode
  def reverse(self):
    current=self.head
    prev=None
    next_node=None 
    while(current is not None):
      next_node=current.next
      current.next=prev
      prev=current 
      current=next_node 
    self.head=prev
  def printf(self):
    temp=self.head 
    while(temp is not None):
      print(temp.data,end=" ")
      temp=temp.next 

def main():
  r=reverse()
  r.atBeg(1)
  r.atBeg(2)
  r.atBeg(3)
  r.atBeg(4)
  r.printf()
  print("after reverse")
  r.reverse()
  r.printf()
if __name__=="__main__":
  main()

