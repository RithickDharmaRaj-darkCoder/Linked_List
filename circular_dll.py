# Data Structure ...
# User-Defined ...
# Linked List ...
# Circular Linked List ...
# Circular-Doubly Linked List ...

class create_node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class C_S_linkedlist:
    def __init__(self,object_name):
        self.name = object_name
        self.head = None
        self.tail = None

    def traversal_fd(self):
        print(f'{self.name} : ',end="")
        h = self.head
        if h:
            while h.next:
                if h.next != self.head:
                    print(f'{h.data} -> ',end="")
                    h = h.next
                else:
                    print(f'{h.data} -> ...')
                    break
        else:
            print(f"Linked List is Empty!")

    def traversal_bw(self):
        print(f'{self.name} : ',end="")
        t = self.tail
        if t:
            while t.prev:
                if t.prev != self.tail:
                    print(f'{t.data} -> ', end="")
                    t = t.prev
                else:
                    print(f'{t.data} -> ...')
                    break
        else:
            print(f"{self.name} : Linked List is Empty!")

    def add_at_starting(self,data):
        newnode = create_node(data)
        h = self.head
        if h:
            newnode.next = self.head
            newnode.prev = newnode.next.prev
            newnode.next.prev = newnode
            while h.next:
                if h.next != self.head:
                    h = h.next
                else:
                    h.next = newnode
                    break
        else:
            newnode.next = newnode
            newnode.prev = newnode
            self.tail = newnode
        self.head = newnode

    def add_at_ending(self,data):
        newnode = create_node(data)
        t = self.tail
        if t:
            newnode.prev = self.tail
            newnode.next = newnode.prev.next
            newnode.prev.next = newnode
            while t.prev:
                if t.prev != self.tail:
                    t = t.prev
                else:
                    t.prev = newnode
                    break
        else:
            newnode.next = newnode
            newnode.prev = newnode
            self.head = newnode
        self.tail = newnode

ll1 = C_S_linkedlist("LL1")
ll1.add_at_starting(30)
ll1.add_at_starting(20)



ll1.traversal_fd()
ll1.traversal_bw()