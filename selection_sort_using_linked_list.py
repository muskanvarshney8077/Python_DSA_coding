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
    def selection(self):
        temp=self.head
        while temp is not None:
            min_index=temp
            temp2=temp.next
            while temp2 is not None:
                if temp2.data<min_index.data:
                   min_index=temp2
                temp2=temp2.next
            temp3=min_index.data
            min_index.data=temp.data
            temp.data=temp3
            temp=temp.next
        
    def printf(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next


def main():
    l=linked()
    l.insert(4)
    l.insert(0)
    l.insert(3)
    l.insert(2)
    l.printf()
    print()
    l.selection()
    l.printf()
if __name__=="__main__":
    main()

