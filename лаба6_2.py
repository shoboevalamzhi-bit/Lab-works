class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def show(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print()
    
    def remove(self, data):
        cur = self.head
        prev = None
        while cur != None:
            if cur.data == data:
                if prev == None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next


if __name__ == "__main__":
    lst = List()
    
    lst.add(10)
    lst.add(20)
    lst.add(30)
    lst.show()
    
    lst.add(5)
    lst.show()
    
    lst.remove(20)
    lst.show()
