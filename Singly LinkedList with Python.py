# Linked List implementation

class Node():
    def __init__(self):
        self.data=None
        self.next=None

    def setData(self,data):
        self.data=data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next=next

    def getNext(self):
        return self.next

    def hasNext(self):
        if self.next==None:
            print("nothing at next")
        else:
            return self.next



class LinkedList():

    def __init__(self,head=None):
        self.head=head
        self.size=0

    def listLength(self):
        current = self.head
        count=0

        while(current!=None):
            count+=1
            current=current.getNext()
        return count

    def size(self):
        return self.size

    def listValues(self):
        values=[]
        current = self.head
        while current!= None:
            values.append(current.getData())
            current=current.getNext()
        print(values)


    def insertAtBeginning(self,data):
        newNode=Node()
        newNode.setData(data)

        if self.size==0:
            self.head=newNode

        else:
            newNode.setNext(self.head)
            self.head=newNode
        self.size+=1
        print("Node added at beginning with value {}".format(data))

    def insertAtLast(self,data):
        newNode=Node()
        newNode.setData(data)

        current=self.head

        while current.getNext() != None:
                current=current.getNext()

        current.setNext(newNode)
        self.size+=1
        print("Node added at Last with value {}".format(data))


mylist=LinkedList()
mylist.insertAtBeginning(12)
mylist.insertAtLast(52)
mylist.insertAtBeginning(13)
mylist.insertAtBeginning(14)
#mylist.insertAtLast(12)
print("LinkedList Length=",mylist.listLength())
#mylist.insertAtBeginning(3)
mylist.listValues()
