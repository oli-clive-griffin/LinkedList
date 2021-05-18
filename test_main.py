import unittest
from main import *

# Although I didn't use any libraries for Linked_list, I assumed I was allowed to use the unittest library for testing.

class Test_Linked_List(unittest.TestCase):
  
  def test_add_first(self):
    test_list = Linked_List(4)

    test_list.add_first(3)
    self.assertEqual(test_list.get_first(), 3)
    
    test_list.add_first("asdf")
    self.assertEqual(test_list.get_first(), "asdf")

    test_list.add_first(None)
    self.assertEqual(test_list.get_first(), None)

    test_list2 = Linked_List()
    test_list2.add_first(2)
    self.assertEqual(test_list2.get_last(), 2)

  def test_add_last(self):
    test_list = Linked_List()

    test_list.add_last(5)
    self.assertEqual(test_list.get_last(), 5)

    test_list.add_last("Hello")
    self.assertEqual(test_list.get_last(), "Hello")

    test_list2 = Linked_List()
    test_list2.add_last(2)
    self.assertEqual(test_list2.get_last(), 2)

  def test_remove_last(self):
    test_list = Linked_List(4)
    test_list.add_last(5)
    test_list.add_last(6)
    self.assertEqual(test_list.remove_last(), 6)    

    test_list2 = Linked_List()
    test_list2.add_last(2)
    self.assertEqual(test_list2.remove_last(), 2)
  
  def test_remove_first(self):
    test_list = Linked_List(4)
    test_list.add_last(5)
    test_list.add_last(6)
    self.assertEqual(test_list.remove_first(), 4)

    test_list2 = Linked_List()
    self.assertEqual(test_list2.remove_first(), None)

    test_list2.add_first(1)
    self.assertEqual(test_list2.remove_first(), 1)


if __name__ == '__main__':
  unittest.main()
