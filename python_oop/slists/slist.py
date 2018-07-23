class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
     
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))

    def removenode(self,value):
        target=Node(value)
        print(target.value)
        head=self.head
        print(head.value)
        if target==head:
            print(head.value)
            head.next=self.head
            target.next = None
            print(head.value)
            return self
      
print("\n\n\n\n================== START OF THE PROGRAM ================")       
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues("Attempt 1")

#Assignment
#Part 1 - recreate SList and Node.  Recreate addNode and printAllValues methods.
#Singly Linked List is one of the most fundamental data structures you'll be using.  Using the concepts here, you'll learn how to create other data structure such as Stacks, Queues, Doubly Linked List, Binary Search Trees, Tries, Graphs, etc.  As it's such a critical concept, please re-create the codes demonstrated above without looking at the platform.  Make sure you feel very comfortable with adding a new Node, traversing through the linked list, etc.  Once you can create both SList and Node without looking at the codes above, then proceed with Part 2.
#part 2 - implement removeNode(val)
#Implement removeNode(val) where it removes a node with the value val.  For example list.removeNode(5) will see if there's a node with the value of 5.  If it is, it will remove that from the linked list.  When you do this, you'll need to consider the following cases:
#
#
#   when the node you want to remove is in the middle of the linked list
#   when the node you want to remove is at the end of the linked list
#
#For each of these cases, you will probably need to have different logics to handle the removal.

list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(1) # removes 1, which is the last node in the list
list.printAllValues("Attempt 1")

As this assignment is quite challenging, it may be good for your to pair up with someone else in your cohort (if available) and do this together.  Please also watch the following video before you start.
Part 3 (optional) - Implement insertNode(val, index)

Implement InsertNode(val, index), which insert a new node of value 'val' on the specified index.  For example, for a linked list with the value of 5 -> 3 -> 1, performing insertNode(7, 2) would insert a Node of value 7 at its 2nd index, making the node 5 -> 3 -> 7 -> 1.

Please make sure that this method allows you to insert a new node as the first node in the list (if index is 0), anywhere in the middle of the list, or at the end of the list (if the specified index is at the end of the list).
START WORKING ON THIS
Privacy Policy
To report a mistake, highlight the selection you believe is in error.

