class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.info, end=">>")
            temp = temp.next

    def insert(self, newinfo):
        newnode = Node(newinfo)
        newnode.next = self.head
        self.head = newnode

    def delete(self, indexlink):
        if self.head == None:
            return
        temp = self.head
        if indexlink == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(indexlink - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def push(self, newinfo):
        newnode = Node(newinfo)
        if self.head is None:
            self.head = newnode
            return
        final = self.head
        while (final.next):
            final = final.next
        final.next = newnode

List = linkedList()
List.push(44)
List.push(36)
List.push(90)
List.push(10)
List.push(60)
List.push(99)


print("Now the list is"),List.printList()
print()
print("----------------------------------------")
print("From exercise must insert 104 to list")
List.insert(104)
print("Now the list is insert 104 "),List.printList()
print()
print("----------------------------------------")
print("Next from exercise must push 57 to list")
List.push(57)
print("Now the list is push 57 "),List.printList()
print("")
print("----------------------------------------")
print("Last from exercise must delete Node 4")
List.delete(4)
print("Now Node4 in the list deleted"),List.printList()
print("")
print("----------------------------------------")
