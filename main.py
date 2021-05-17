import doubly

linkedList = doubly.DoublyLinkedList()

# INSERTION
print("INSERTION")
linkedList.insertData(50)
linkedList.addNodeBeginning(100)
linkedList.addNodeEnd(5)
linkedList.addNodeInPos(88,4)
linkedList.printList()

# DELETION
print("DELETION")
linkedList.deleteFirstNode()
linkedList.deleteLastNode()
linkedList.deleteNodeByPos(1)
linkedList.printList()

# TRAVERSING WHILE PRINTING THE LIST (bOTH FORWARD AND BACK WORD)
print("TRAVERSING")
linkedList.forwardTravel()
linkedList.backWordTravel()
linkedList.printList()

# SEARCHING FOR THE GIVEN WITH PRINTING THE POSITION THE NODE
print("SEARCHING")
linkedList.findData(4)

