from linked_list import Node, LinkedList
import string

f = open("text.txt", "r") ## loads IOStream to f
line = f.read()
table = str.maketrans(string.punctuation, "                                ")
newline = line.translate(table).lower()

def getWordList(line):                                  # O(n)
    wordList = LinkedList()
    temp = ''
    for char in line:
        if char != ' ':
            temp = temp + char
        else:
            if temp != '':
                wordList.addNodeE(Node(temp))
                temp = ''
    return wordList

def getNumList(line):                                   # O(n)
    numList = LinkedList()
    for num in line:
        numList.addNodeE(Node(num))
    return numList

def mergeSort(lt):                                      # O(nlogn)
    if lt.len < 2:
        return lt
    elif lt.len == 2:
        if lt.head.val < lt.end.val:
            return lt
        else:
            sorted_lt = LinkedList()
            sorted_lt.addNodeH(Node(lt.end.val))
            sorted_lt.addNodeE(Node(lt.head.val))
            return sorted_lt
    else:
        a,b = divideList(lt)
        sorted_a = mergeSort(a)
        sorted_b = mergeSort(b)
        return sortedMerge(sorted_a,sorted_b)

def divideList(lt):                                     # O(len(lt)/2)
    half_index = int(lt.len/2.0)
    a = LinkedList()
    for i in range(half_index):
        a.addNodeE(Node(lt.head.val))
        lt.delNodeH()
    return a, lt

def sortedMerge(a,b):                                   # O(len(a)+len(b))                                  
    sorted_list = LinkedList()
    while a.len !=0 and b.len !=0:
        if a.head.val < b.head.val:
            sorted_list.addNodeE(Node(a.head.val))
            a.delNodeH()
        else:
            sorted_list.addNodeE(Node(b.head.val))
            b.delNodeH()
    if a.len == 0:
        sorted_list.addNodeE(b.head)
    else:
        sorted_list.addNodeE(a.head)
    return sorted_list

x = getWordList(newline)
x = mergeSort(x)

l = [2,6,2340,734,723,886,4,55]
y = getNumList(l)
y = mergeSort(y)
