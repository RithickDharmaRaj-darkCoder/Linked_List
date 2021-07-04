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
        print(f'{self.name}-Tf : ',end="")
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
        print(f'{self.name}-Tb : ',end="")
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
            print(f"Linked List is Empty!")

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

    def add_before(self,data,x):
        h = self.head
        if not h:
            print(f"{self.name} : Linked List is Empty!")
        else:
            if h.data == x:
                self.add_at_starting(data)
            else:
                while h.next:
                    if h.next.data == x:
                        newnode = create_node(data)
                        newnode.next = h.next
                        h.next = newnode
                        newnode.prev = newnode.next.prev
                        newnode.next.prev = newnode
                        break
                    elif h.next.data != x and h.next.next == self.head:
                        print(f"{self.name} : {x} is not in the Linked List!")
                        break
                    else:
                        h = h.next

    def add_after(self,data,x):
        t = self.tail
        if not t:
            print(f"{self.name} : Linked List is Empty!")
        else:
            if t.data == x:
                self.add_at_ending(data)
            else:
                while t.prev:
                    if t.prev.data == x:
                        newnode = create_node(data)
                        newnode.prev = t.prev
                        t.prev = newnode
                        newnode.next = newnode.prev.next
                        newnode.prev.next = newnode
                        break
                    elif t.prev.data != x and t.prev.prev == self.tail:
                        print(f"{self.name} : {x} is not in the Linked List!")
                        break
                    else:
                        t = t.prev

    def del_at_starting(self):
        h = self.head
        if not h:
            print(f"{self.name} : Linked List is already Empty!")
        else:
            if h.next == self.head:
                self.head = None
                self.tail = None
                print(f"{self.name} : Linked List is made Empty!")
            else:
                root = h.next
                root.prev = h.prev
                while h.next:
                    if h.next != self.head:
                        h = h.next
                    else:
                        h.next = root
                        break
                self.head = root
