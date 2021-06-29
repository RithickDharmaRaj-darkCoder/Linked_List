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