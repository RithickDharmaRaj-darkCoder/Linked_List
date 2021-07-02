# Data Structure ...
# User-Defined ...
# Linked List ...
# Circular Linked List ...
# Circular-Singly Linked List ...

class create_node:
    def __init__(self,data):
        self.data = data
        self.next = None

class C_S_linkedlist:
    def __init__(self,object_name):
        self.name = object_name
        self.head = None

    def traversal(self):
        print(f'{self.name} : ',end= "")
        h = self.head
        while h:
            print(f'{h.data} -> ',end= "")
            h = h.next
            if h == self.head:
                print('...')
                break
        else:
            print('Linked List is Empty!')

    def add_ll_empty(self,data):
        n = self.head
        if n:
            print(f'{self.name} : Linked List is not Empty!')
        else:
            newnode = create_node(data)
            newnode.next = newnode
            self.head = newnode

    def add_at_starting(self,data):
        newnode = create_node(data)
        newnode.next = self.head
        h = self.head
        if not h:
            newnode.next = newnode
        else:
            while h.next != self.head:
                h = h.next
            h.next = newnode
        self.head = newnode

    def add_at_ending(self,data):
        newnode = create_node(data)
        newnode.next = self.head
        h = self.head
        if not h:
            newnode.next = newnode
            self.head = newnode
        else:
            while h.next != self.head:
                h = h.next
            h.next = newnode

    def add_after_node(self,data,x):
        h = self.head
        while h:
            if h.data == x and h.next != self.head:
                break
            if h.data == x and h.next == self.head:
                break
            if h.data !=x and h.next == self.head:
                print(f'{self.name} : {x} is not in the linked list')
                break
            else:
                h = h.next
        else:
            print(f'{self.name} : Linked List is Empty!')