# Data Structure ...
# User-Defined ...
# Linked List ...
# Doubly Linked List ...

class create_node():
    def __init__(self,data):
        self.linktoP = None
        self.data = data
        self.linktoN = None

class D_LinkedList():
    def __init__(self,Object_Name):
        self.name = Object_Name
        self.head = None
        self.tail = None

    def traversal_Forword(self):
        print(f'{self.name} : ',end= " ")
        if self.head is None:
            print('Linked List is Empty!')
        else:
            node = self.head
            print(f'Head -> ',end= " ")
            while node is not None:
                print(f'{node.data} -> ',end= " ")
                node = node.linktoN
            print('Tail\n--------------------')

    def traversal_Backword(self):
        print(f'{self.name} : ',end= " ")
        if self.head is None:
            print('Linked List is Empty!')
        else:
            node = self.tail
            print(f'Tail -> ',end= " ")
            while node is not None:
                print(f'{node.data} -> ', end=" ")
                node = node.linktoP
            print('head\n--------------------')

    def add_at_starting(self, data):
        newnode = create_node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode

        else:
            newnode.linktoN = self.head
            newnode.linktoN.linktoP = newnode
            self.head = newnode

    def add_at_ending(self,data):
        newnode = create_node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            h = self.head
            t = self.tail
            while h is not  None:
                h = h.linktoN
            else:
                newnode.linktoP = self.tail
                self.tail = newnode
                newnode.linktoP.linktoN = newnode

    def add_LL_empty(self,data):
        if self.head is not None:
            print(f'{self.name} : Linked List is not Empty!')
        else:
            self.add_at_starting(data)

    def add_after_node(self,data,x):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            h = self.head
            while h is not None:
                if h.data == x and h.linktoN == None:
                    self.add_at_ending(data)
                    break
                elif h.data != x and h.linktoN is not None:
                    h = h.linktoN
                elif h.data != x and h.linktoN is None:
                    print(f'{x} is not in the Linked List!')
                    break
                elif h.data == x and h.linktoN is not None:
                    newnode = create_node(data)
                    newnode.linktoN = h.linktoN
                    h.linktoN = newnode
                    newnode.linktoP = newnode.linktoN.linktoP
                    newnode.linktoN.linktoP = newnode
                    break

    def add_before_node(self,data,x):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            t = self.tail
            while t is not None:
                if t.data == x and t.linktoP is None:
                    self.add_at_starting(data)
                    break
                elif t.data != x and t.linktoP is not None:
                    t = t.linktoP
                elif t.data != x and t.linktoP is None:
                    print(f'{x} is not in the Linked List!')
                    break
                elif t.data == x and t.linktoP is not None:
                    newnode = create_node(data)
                    newnode.linktoP = t.linktoP
                    t.linktoP = newnode
                    newnode.linktoN = newnode.linktoP.linktoN
                    newnode.linktoP.linktoN = newnode
                    break

    def del_at_starting(self):
        if self.head is None:
            print(f'{self.name} : Linked List is already Empty!')
        else:
            if self.head.linktoN is None:
                self.head = None
                self.tail = None
                print(f'{self.name} : Linked List is made Empty!')
            else:
                h = self.head
                self.head = h.linktoN
                h.linktoN.linktoP = h.linktoP