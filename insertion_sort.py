from doubly_linked_list import DoublyLinkedList, Node
import string

"""
Input example:
2 4
4 1
9 2 5
1 5

i.e.
1) Takes the values of each line and perform a multiplication
2) Insertion sort the result with a doubly linked list implementation

Output example:
[4,5,8,90]

"""
def insertion_sort(lt, val):
    if lt.len == 0:
        lt.addNodeE(Node(val))
    else:
        current = lt.head
        while True:
            if current.val <= val:
                if current.next != None:
                    current = current.next
                else:
                    lt.addNodeE(Node(val))
                    break
            else:
                node = Node(val)
                temp = current.prev
                current.setPrev(node)
                node.setNext(current)
                if temp != None:
                    node.setPrev(temp)
                    temp.setNext(node)
                else:
                    lt.head = node
                lt.len += 1
                break
    return lt

lt = DoublyLinkedList()
f = open("insertion_example.txt", "r")
for line in f:
    product = 1
    for char in line:
        if char == '\n':
            break
        elif char != ' ':
            product *= int(char)
    insertion_sort(lt, product)

lt.print()
