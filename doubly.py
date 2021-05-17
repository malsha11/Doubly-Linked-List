# create node class
class Node:
    def __init__(self, data):
        self.data = data
        self.nextRef = None
        self.prevRef = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Forward Traversing the doubly linked List
    def forwardTravel(self):
        if self.head is None:
            print("Empty Doubly linked list")
        else:
            current = self.head
            while current is not None:
                print(current.data, " ")
                current = current.nextRef

    # Back ward Traversing the doubly linked List
    def backWordTravel(self):
        if self.head is None:
            print("Empty Doubly linked list")
        else:
            current = self.head
            while current.nextRef is not None:
                current = current.nextRef
            while current is not None:
                print(current.data)
                current = current.prevRef

    # Insert data for empty Linked List
    def insertData(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("Linked List is not empty!")

    # Insert an item Beginning
    def addNodeBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextRef = self.head
            self.head.preRef = newNode
            self.head = newNode
        print()

    # Inset an item End
    def addNodeEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.nextRef is not None:
                current = current.nextRef
            current.nextRef = newNode
            newNode.prevRef = current
        print()

    def addNodeInPos (self, data , pos):
        newNode = Node(data)
        # if the position is > 0
        if pos < 1:
            print("position should be >= 1.")
        elif pos == 1:
            #if the position is 1, make new node as head
            newNode.nextRef = self.head
            self.head.prevRef = newNode
            self.head = newNode
        else:
            temp = self.head
            for i in range(1 , pos-1):
                if temp != None:
                    temp = temp.nextRef

            #If the previous node is not null, adjust
            if(temp != None):
                newNode.nextRef = temp.nextRef
                newNode.prevRef = temp
                temp.nextRef = newNode
                if (newNode.nextRef != None):
                    newNode.nextRef.prevRef = newNode
                else:
                    # When the previous node is null
                    print("The previous node is null.")
    # delete an item in the beginning
    def deleteFirstNode(self):
        # if doubly linked list is Empty
        if self.head is None:
            print("Empty Linked List")
            return
        # if doubly linked list contant only one Node
        if self.head.nextRef is None:
            self.head = None
            print("Can't delete because list has only one Node")
        # if doubly linked list content more than one Node
        else:
            self.head = self.head.nextRef
            self.head.prevRef = None

    def deleteLastNode(self):
        # if doubly linked list is Empty
        if self.head is None:
            print("Empty Linked List")
            return
        # if doubly linked list contant only one Node
        if self.head.nextRef is None:
            self.head = None
            print("Can't delete because list has only one Node")
        # if doubly linked list content more than one Node
        else:
            current = self.head
            while current.nextRef is not None:
                current = current.nextRef
            current.prevRef.nextRef = None

    # Delete an item given position
    def deleteNodeByPos(self, pos):
        # if doubly linked list is Empty
        if self.head is None:
            print("Empty Linked List")
            return
        # if doubly linked list contant only one Node
        if self.head.nextRef is None:
            if pos == self.head.data:
                self.head = None
            else:
                print("Can't delete because position is not present")

        # if doubly linked list content more than one Node

        if self.head.data == pos:
            self.head = self.head.nextRef
            self.head.prevRef = None

        current = self.head
        while current.nextRef is not None:
            if pos == current.data:
                break
            current = current.nextRef

        if current.nextRef is not None:
            current.nextRef.prevRef = current.prevRef
            current.prevRef.nextRef = current.nextRef
        else:
            if current.data == pos:
                current.prevRef.nextRef = None
            else:
                print(" Not Present")

    # Find a data
    def findData(self, data):
        current = self.head
        while current:  # while the current node is not None
            if current.data == data:
                print(f"{data} Found.")
                return
            else:
                current = current.nextRef
        else:
            print(f"{data} Not Found.")

    #print Function
    def printList(self):
        if self.head is None:
            print("Empty linked list")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.nextRef





