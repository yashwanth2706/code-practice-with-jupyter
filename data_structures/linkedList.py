class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next != None:
            current = current.next
        current.next = new_node
        
    def delete(self, id):
        if id < 0:
            print(f"Node index cannot be Negative")
            return
        current = self.head
        if id == 0:
            self.head = current.next
            return
        if (current is None) or (current.next is None):
            print(f"Node index outof range")
            return
        id -= 1
        while current != None:
            if current.data == id:
                current.next = current.next.next
                return
            current = current.next
            if current.next is None:
                print(f"{id+1} List index out of range")
                return
                    
    def update(self, data, new_data):
        current = self.head
        while current != None:
            if current.data == data:
                current.data = new_data
                break                
            if current.next is None:
                print(f"{data} is not available in the list")
            current = current.next

    def print_list(self):
        current = self.head
        while current != None:
            print(f"{current.data}->", end="")
            current = current.next
        print(current)
        return
    
ll = LinkedList()
ll.insert(0)
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.print_list()
ll.delete(5)
ll.print_list()
ll.update(7, 100)
ll.update(2, 22)
ll.print_list()
