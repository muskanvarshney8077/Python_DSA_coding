class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class stack:
  def __init__(self):
    self.tos=-1 
    self.head=None 
  def empty(self):
    if (self.head is None):
      return True
    return False 
  def push(self,data):
    newNode=node(data)
    if self.head is None:
      self.head =newNode
      self.tos+=1
      return
    else:
      newNode.next=self.head
      self.head=newNode
      self.tos+=1 
  def pop(self):
    if self.empty():
      print("stack is empty")
      return
    self.head=self.head.next 
    self.tos-=1 
  def size(self):
    return self.tos+1 

  def top(self):
    if self.empty():
      return False
    return self.head.data 

def main():
  st=stack()
  for ele in input().split():
    st.push(int(ele))
  print(st.size)
  while(st.size()!=0):
    print(st.top())
    st.pop()
    print()
if __name__=="__main__":
  main()