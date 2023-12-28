from node import Node

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        current = self.head
        
        while current.next !=None:
            current = current.next
        current.next = new_node
    
    def length(self):
        current = self.head
        total = 0
        while current.next !=0:
            total+=1
            current = current.next
        return total
    
    def show(self):
        current = self.head
        elements = ""
        while current.next!=None:
            current = current.next
            elements+=str(current.data)
        print(elements)
    
    def get(self, index):
        if index >=self.length():
            print("ERROR: 'Get' Index out of range")
            return None
        
        cur_indx = 0
        current = self.head
        while True:
            current = current.next
            if cur_indx == index: return current.data
            cur_indx+=1