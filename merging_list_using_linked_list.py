import sys
sys.setrecursionlimit(100000000)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def insertAtBeg(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
            
        return self.head
    def printf(self,head):
        temp=head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
        
def merge(head1,head2):
    if head1 == None and head2== None:
        return None
    elif head1==None:
        return head2
    elif head2==None:
        return head1
    else:
        if head1.data<head2.data:
            temp=head1
            temp.next=merge(head1.next,head2)
        else:
            temp=head2
            temp.next=merge(head1,head2.next)
    return temp
    
def main():
    s1=linkedList()
    s2=linkedList()
    for ele in input().split():
        head1=s1.insertAtBeg(ele)
    for ele in input().split():
        head2=s2.insertAtBeg(ele)
    head=merge(head1,head2)
    s1.printf(head)

if __name__=="__main__":
    main()
    
