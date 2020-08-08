class Node :
    def __init__(self, data=None) :
        self.data = data
        self.next = None

class Queue :
    def __init__ (self) :
        self.head = Node()
    
    def insert(self, data) :
        NewNode = Node(data)
        key = self.head
        while key.next != None :
            key = key.next
        key.next = NewNode

    def pop (self) :
        toPop = self.head.next
        toReturn = toPop.data
        self.head.next = toPop.next

        return toReturn

    def show(self) :
        key = self.head
        string = "Start\n v"
        while key.next != None :
            key = key.next
            string += f"\n {key.data} "
        print(string)

