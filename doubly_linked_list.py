class Node():
    # Initialise node properties
    def __init__(self, data):           ## O(1)
        self.val = data
        self.next = None
        self.prev = None
        
    # Set node's value
    def setVal(self,val):               ## O(1)
        self.val = val

    # Set node's link
    def setNext(self,next_node):        ## O(1)
        self.next = next_node

    def setPrev(self, prev_node):       ## O(1)\
        self.prev = prev_node

class DoublyLinkedList():
    def __init__(self):                 ## O(1)
        self.head = None
        self.end = None
        self.len = int()

    def addNodeH(self,node):            ## O(1)
        assert isinstance(node, Node)
        
        ## Add node to front
        
        if self.len > 0:
            self.head.setPrev(node)
            node.setNext(self.head)
            self.head = node
            self.len += 1
        else:
            self.head = node
            self.end = node
            self.len += 1

    def addNodeE(self,node):            ## O(1)
        assert isinstance(node, Node)
        
        ## Add node to end
        
        if self.len > 0:
            self.end.setNext(node)
            node.setPrev(self.end)
            self.end = self.end.next
            self.len += 1
        else:
            self.head = node
            self.end = node
            self.len += 1

    def addNodeNext(self, node, loc_val): ## O(n)

        ## Add node to specific location's front

        current = self.head
        if current == None:
            print ("Empty List")
        else: 
            while True:
                if current == None:
                    print("Element not found.")
                    break
                elif current.val == loc_val:
                    temp = current.next
                    current.setNext(node)
                    node.setPrev(current)
                    if temp != None:
                        node.setNext(temp)
                        temp.setPrev(node)
                    else:
                        self.end = node
                    self.len += 1
                    break
                else:
                    current = current.next

    def addNodePrev(self, node, loc_val): ## O(n)

        ## Add node to specific location's front

        current = self.head
        if current == None:
            print ("Empty List")
        else: 
            while True:
                if current == None:
                    print("Element not found.")
                    break
                elif current.val == loc_val:
                    temp = current.prev
                    current.setPrev(node)
                    node.setNext(current)
                    if temp != None:
                        node.setPrev(temp)
                        temp.setNext(node)
                    else:
                        self.head = node
                    self.len += 1
                    break
                else:
                    current = current.next

    def delNodeH(self):                 ## O(1)
        if self.head != None:
            if self.len == 1:
                self.head = None
                self.end = None
                self.len = 0
            else:
                self.head = self.head.next
                self.head.prev.setNext(None)
                self.head.setPrev(None)
                self.len -= 1
        else:
            print ("Empty List")

    def delNodeE(self):                 ## O(1)
        if self.end != None:
            if self.len == 1:
                self.head = None
                self.end = None
                self.len = 0
            else:
                self.end = self.end.prev
                self.end.next.setPrev(None)
                self.end.setNext(None)
                self.len -= 1
        else:
            print ("Empty List")

    def delNodeS(self, loc_val):       ## O(n)

        ## Delete node from specific location
        
        current = self.head
        if current == None:
            print ("Empty List")
        else:
            while True:
                if current == None:
                    print("Element not found")
                    break
                elif current.val == loc_val:
                    if self.len == 1:
                        self.head = None
                        self.end = None
                        self.len = 0
                    else:
                        if current.prev == None:
                            self.head = self.head.next
                            self.head.prev.setNext(None)
                            self.head.setPrev(None)
                            self.len -= 1
                        elif current.next == None:
                            self.end = self.end.prev
                            self.end.next.setPrev(None)
                            self.end.setNext(None)
                            self.len -=1
                        else:
                            current.prev.setNext(current.next)
                            current.next.setPrev(current.prev)
                            current.setNext(None)
                            current.setPrev(None)
                            self.len -= 1
                    break
                else:
                    current = current.next

    def print(self):                ## O(n)
        lt = []
        current = self.head
        while True:
            if current == None:
                break
            else:
                lt.append(current.val)
                current = current.next
        print (lt)

    def printLen(self):                 ## O(1)
        print (self.len)
