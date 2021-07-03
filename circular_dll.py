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
        h = self.head
        if h:
            while h.next:
                if h.next != self.head:
                    print(f'{self.name} : {h.data} -> ',end="")
                    h = h.next
                else:
                    print(f'{self.name} : {h.data} -> ...')
                    break
        else:
            print(f"{self.name} : Linked List is Empty!")

    def traversal_bw(self):
        t = self.tail
        if t:
            while t.prev:
                if t.prev != self.tail:
                    print(f'{self.name} : {t.data} -> ', end="")
                    t = t.prev
                else:
                    print(f'{self.name} : {t.data} -> ...')
                    break
        else:
            print(f"{self.name} : Linked List is Empty!")