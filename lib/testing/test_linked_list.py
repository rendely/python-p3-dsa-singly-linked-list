from linked_list import LinkedList

class TestLinkedList:
    '''Class LinkedList in linked_list.py'''

    def test_hello(self):
        '''Tests hello()'''
        assert LinkedList.hello() == 'hello'
    
    def test_test_nothing(self):
      '''Tests nothing'''
      assert 'not hi' != 'hi'