#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item
        node = Node(item)
        if self.is_empty():
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        previous = None
        current = self.head
        while current is not None:
            if current.data is item:
                if self.head is current:
                    self.head = current.next
                if self.tail is current:
                    self.tail = previous
                if previous:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        raise ValueError("Could not find item in LinkedList")

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        for item in self.as_list():
            if quality(item) is True:
                return item
            if quality(item) is None:
                raise ValueError("Item not found")


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())
    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
