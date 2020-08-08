class Node :
    def __init__(self, data=None) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self) :
        self.head = Node()
    
    def insert_first (self, data) :
        NewNode = Node(data)
        NewNode.next = self.head.next
        self.head.next = NewNode
    
    def insert_last (self, data) :
        NewNode = Node(data)
        key = self.head
        while key.next != None :
            key = key.next
        #key.next is None and key.data has last value
        key.next = NewNode
    
    def insert (self, data , index = 0) :
        # Inserts data after the given index
        if index == 0 :
            self.insert_first(data)
            return
        if index == -1 :
            self.insert_last (data)
            return
        if index > self.length() :
            print("ERROR, index out of range !")
            return
        NewNode = Node(data)
        current_index = 1
        key = self.head
        while key.next != None :
            key = key.next
            if current_index == index :
                NewNode.next = key.next
                key.next = NewNode
                break
            current_index += 1
    
    def delete (self, index) :
        if index >= self.length() :
            print ("ERROR, index out of range !")
            return
        current_index = 0
        current_node = self.head
        while True :
            last_node = current_node
            current_node = current_node.next
            if current_index == index :
                last_node.next = current_node.next
                return
            current_index += 1

    def get (self ,index) :
        if index >= self.length() :
            print ("ERROR, index out of range !")
            return
        current_index = 0
        key = self.head
        while True :
            key=key.next
            if current_index == index :
                return key.data
            current_index += 1

    def show(self) :
        key = self.head
        string = ""
        while key.next != None :
            key = key.next
            string += f"\n{key.data}"
        string += " <-- START"
        print(string)


    def length (self):
        count = 0
        key = self.head
        while key.next != None :
            count += 1
            key = key.next
            
        return count
    
    
