# Data Structure ...
# User-Defined ...
# Linked List ...
# Singly Linked List (Adding data @ Ending) ...

class creatingnode():
    def __init__(self,data):
        self.data = data
        self.linkto = None

class linkedlist():
    def __init__(self,object_name):
        self.name = object_name
        self.head = None

    def traversal(self):
        print(self.name, end=" ")
        if self.head is None:
            print('Linked List is Empty!\n--------------------')
        else:
            print('Head --> ', end=" ")
            n = self.head
            while n is not None:
                print(f'[{n.data}] --> ',end=" ")
                n = n.linkto
            print('None')
            print('--------------------')

    def add_at_starting(self,data):
        newnode = creatingnode(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.linkto = self.head
            self.head = newnode


    def add_at_ending(self,data):
        newnode = creatingnode(data)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.linkto is not None:
                n = n.linkto
            n.linkto = newnode


    def add_after_node(self,data,x):
        newnode = creatingnode(data)
        n = self.head
        if self.head is None:
            print(self.name, end=" ")
            print('No Node in the Linked List!\n--------------------')
        else:
            while (n.data != x) and (n.linkto is not None):
                n = n.linkto
            else:
                if n.data == x:
                    newnode.linkto = n.linkto
                    n.linkto = newnode

                else:
                    print(self.name, end=" ")
                    print(f'{x} is not in the Linked List!\n--------------------')

    def add_before_node(self,data,x):
        n = self.head
        if n is None:
            print(self.name, end=" ")
            print('No Node in the Linked List!\n--------------------')
        elif n.data == x:
            self.add_at_starting(data)
        else:
            while n.linkto is not None:
                if n.linkto.data == x:
                    self.add_after_node(data,n.data)
                    break
                else:
                    n = n.linkto
            if n.linkto is None:
                print(self.name, end=" ")
                print(f'{x} is not in the Linked List!\n--------------------')

    def add_when_LL_Empty(self,data):
        if self.head is None:
            self.add_at_starting(data)
        else:
            print(self.name, end=" ")
            print("Linked List is not empty!\n--------------------'")

    def del_at_starting(self):
        if self.head is None:
            print(self.name, end=" ")
            print("Linked List is already empty!\n--------------------'")
        else:
            self.head = self.head.linkto

    def del_at_ending(self):
        if self.head is None:
            print(self.name, end=" ")
            print("Linked List is already empty!\n--------------------'")
        else:
            n = self.head
            if n.linkto == None:
                self.head = None
            else:
                while n.linkto.linkto != None:
                    n = n.linkto
                n.linkto = None

    def del_Node(self,x):
        if self.head is None:
            print(self.name, end=" ")
            print("Linked List is already empty!\n--------------------'")
        else:
            n = self.head
            if n.data == x:
                self.del_at_starting()
            else:
                while n.linkto != None:
                    if n.linkto.data != x:
                        n = n.linkto
                    else:
                        n.linkto = n.linkto.linkto
                        break
                else:
                    if n.linkto == None:
                        print(self.name, end=" ")
                        print(f'{x} is not in the Linked List!\n--------------------')
