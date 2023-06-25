import pytest
from linked_list import Node, LinkedList


class TestLinkedList:
    '''Class LinkedList in linked_list.py'''

    def test_Node(self):
        '''Tests Node class'''
        hello = Node('Hello')
        assert isinstance(hello, Node)
        assert hello.data == 'Hello'
    
    def test_LinkedList(self):
      '''Tests LinkedList class'''
      hello = Node('Hello')
      my_list = LinkedList(hello)
      assert my_list.head == hello

    def test_append(self):
      '''Tests append()'''
      first = Node('one')
      second = Node('two')
      my_list = LinkedList(first)
      my_list.append(second)
      assert first.next_node == second

    def test_repr(self, capsys):
      '''tests the __repr__'''
      first = Node('one')
      print(first)
      out, err = capsys.readouterr()
      assert out == 'Node(data=one)\n'
      my_list = LinkedList(first)
      print(my_list)
      out, err = capsys.readouterr()
      assert out == 'LinkedList(head=Node(data=one))\n'