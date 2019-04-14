#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    if position == 0:
        current_node = SinglyLinkedListNode(data, head)
        return current_node
    else:
        prev = head
        curr = head.next
        count = 1
        while count < position:
            prev = curr
            curr = curr.next
            count += 1
        new_node = SinglyLinkedListNode(data)
        prev.next = new_node
        new_node.next = curr
        return head
# How to optimise the code, other edge use cases?

if __name__ == '__main__':
    pass