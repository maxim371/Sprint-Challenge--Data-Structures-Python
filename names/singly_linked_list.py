'''0(1) - beg, 0(n) - end - insertion/remove
   0(1) - array, 0(n) - search 
   0(n) - array - insert beg
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.value , " ")
                n = n.next_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node


    def remove_head(self):
        if self.head is None:
            return None
        else:
            if self.head.get_next_node() is None:
                h = self.head
                self.head = None
                self.tail = None
                return h.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next_node()
        return value    




    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node


    def remove_tail(self):    
        if self.head is None:
            return None
        value = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.next_node.get_next_node() is not None:
            current = current.next_node
        self.tail = current
        return value




  
