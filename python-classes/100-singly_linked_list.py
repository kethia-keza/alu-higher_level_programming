#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node and class SinglyLinkedList for a sorted singly linked list.
"""


class Node:
    """Class Node that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """String representation of the linked list for printing."""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
