# Creating linked list data structure
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # function to insert the data in the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given the reference to the head of the list and key
    def delete_node(self, key):
        # Store head node
        tmp = self.head

        if (tmp is not None):
            if (tmp.data == key):
                self.head = tmp.next
                tmp = None
                return
        # search for key
        while(tmp is not None):
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next

        if (tmp == None):
            return

        # Unlink the node from linked list
        prev.next = tmp.next

        tmp = None

    # function to find the length of the list
    def get_count(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

    # function to search
    def search(self, key):
        current = self.head

        #loop over the list
        while(current is not None):
            if current.data == key:
                return True
            current = current.next

        return False

    # function to print the linked list
    def print_list(self):
        temp = self.head

        while(temp):
            print("%d" % temp.data)
            temp = temp.next

    # 4. Function to getNth element of the list
    def get_nth(self, index):
        current = self.head
        count = 0

        while(current):
            if count == index:
                return current.data
            count += 1
            current = current.next

        assert(False)
        return 0

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    print("Print the list: ")
    llist.print_list()
    print("The lenght of the list %d " % llist.get_count())

    # Delete the node
    print("Deleting the node: ")
    llist.delete_node(1)
    llist.print_list()
    print("The lenght of the list %d " % llist.get_count())

    # search the element in linked list
    print(llist.search(10))
    print(llist.search(3))

    # 4. getNth element
    print(llist.get_nth(1))