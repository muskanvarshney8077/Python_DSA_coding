
class stack:
  def __init__(self):
    self.arr=[]
    self.tos=-1 
  def push(self,data):
    self.tos+=1 
    self.arr.append(data)
  def empty(self):
    return self.tos==-1
  def pop(self):
    if self.empty():
      return
    else:
      self.tos-=1
      self.arr.pop()
  def top(self):
    return self.arr[self.tos]
  def size(self):
    return self.tos+1 
def main():
  st=stack()
  for ele in input().split():
    st.push(int(ele))
  print(st.size())
  while(st.size()!=0):
    print(st.top())
    st.pop()
if __name__=="__main__":
  main()

    