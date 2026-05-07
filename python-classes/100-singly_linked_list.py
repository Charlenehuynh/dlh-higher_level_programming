#!/usr/bin/python3
"""This module create a single linked list by module."""


class Node:
    """ This class represent data and pointer of node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ This class create a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        # 1.Empty list (head is None)->create new Node and assign head to node
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
            return
        # 2. Value <= head (new->head then head to new)
        if value <= self.__head.data:
            new_node = Node(value, self.__head)
            self.__head = new_node
            return
        # 3. Middle or end where value > head. Create pointer
        # current and traverse until next is none or current.data >= value
        if value > self.__head.data:
            current = self.__head
            while (current.next_node is not None
                   and current.next_node.data < value):
                current = current.next_node
            new_node = Node(value, current.next_node)
            current.next_node = new_node
            return

    # represent object as string for print
    def __str__(self):
        result = ""
        current = self.__head
        while current is not None:
            result = result + str(current.data) + "\n"
            current = current.next_node
        new_result = result.rstrip("\n")
        return new_result
