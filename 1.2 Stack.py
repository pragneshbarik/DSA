class Node :
    def __init__ (self, data = None) :
        self.data = data
        self.next = None

class Stack :
    def __init__(self) :
        self.head = Node()

    def push(self, data) :
        NewNode = Node(data)
        NewNode.next = self.head.next
        self.head.next = NewNode
    
    def pop(self) :
        toPop = self.head.next
        toReturn = toPop.data
        self.head.next = toPop.next
        
        return toReturn

    def show(self) :
        key = self.head
        string = ""
        while key.next != None :
            key = key.next
            string += f"\n {key.data} "
        string += " <--First In"
        print(string)



