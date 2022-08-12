# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from linear.linkedlist import SinglyLinkedList

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = [12, 23,34,45,56]

    linked_list = SinglyLinkedList()

    for i in data:
        linked_list.add(i)
    for elem in linked_list.traverse():
        print(elem)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
