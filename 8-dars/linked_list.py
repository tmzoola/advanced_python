class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        current = self.head
        
        while current.next !=None:
            current = current.next
        current.next = new_node
    
    def show(self):
        current = self.head
        elements = ""
        
        while current.next != None:
            current= current.next
            elements += str(current.data)
        return elements
    

my_list = LinkedList()

my_list.append(2)
my_list.append(2)
my_list.append(4)

print(my_list.show())


