

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def add(self, data):
        ''' Adding the element to the list
        :param data - value to be added in the list
        '''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        '''
        Iterate and yields the element value from the list
        :return: None
        '''
        cur = self.head
        while cur.next != None:
            yield cur.data
            cur = cur.next

    def search(self, value):
        '''
        Search the given value in the list
        :param value: searchable value
        :return: boolean true or false
        '''
        cur = self.head
        while cur != None and cur.data != value:
            cur = cur.next
        if cur is None:
            return False
        return True







