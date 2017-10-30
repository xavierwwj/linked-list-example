class Node():
    # Initialise node properties
    def __init__(self, data):           ## O(1)
        self.val = data
        self.next = None
        
    # Set node's value
    def setVal(self,val):               ## O(1)
        self.val = val

    # Set next node's link
    def setNext(self,next_node):        ## O(1)
        self.next = next_node

class LinkedList():
    def __init__(self):                 ## O(1)
        self.head = None
        self.end = None
        self.len = int()

    def addNodeH(self,node):            ## O(1)

        ## Add node to front

        if self.len > 0:
            node.setNext(self.head)
            self.head = node
            self.len += 1
        else:
            self.head = node
            self.end = node
            self.len += 1

    def addNodeE(self,node):            ## O(1)

        ## Add node to end
        if self.len < 1:
            self.head = node
            self.end = node
            self.len += 1
        else:
            self.end.setNext(node)
            self.end = self.end.next
            self.len += 1

    def addNodeS(self, node, location): ## O(n)

        ## Add node to specific location

        assert isinstance(location, int)
        current = self.head
        while True:
            if current == None:
                print("Element not found.")
                break
            elif current.val == location:
                temp = current.next
                current.next = node
                node.next = temp
                self.len += 1
                break
            else:
                current = current.next

    def delNodeH(self):                 ## O(1)
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.setNext(None)
            self.len -= 1
        else:
            print ("Empty List")

    def delNodeE(self):                 ## O(n)
        self.delNodeS(self.end.val)

    def delNodeS(self, location):       ## O(n)

        ## Delete node from specific location
        
        assert isinstance(location, int)
        current = self.head
        if current == None:
            print ("Empty List")
        else: 
            prev = None
            while True:
                if current == None:
                    print("Element not found")
                    break
                elif current.val == location:
                    if current == self.head:
                        temp = self.head
                        self.head = self.head.next
                        temp.setNext(None)
                        self.len -= 1
                        break
                    elif current == self.end:
                        prev.next = None
                        self.end = prev
                        self.len -= 1
                        break
                    else:
                        prev.next = current.next
                        current.setNext(None)
                        self.len -= 1
                        break
                else:
                    prev = current
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
