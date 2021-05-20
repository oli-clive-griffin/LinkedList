import unittest
from main import *



class Test_Linked_List(unittest.TestCase):
  
  def test_add_first(self):
    test_list = Linked_List()
    test_list.add_first(3)
    self.assertEqual(test_list.get_first(), 3)

    test_list2 = Linked_List()
    test_list2.add_first(2)
    self.assertEqual(test_list2.get_last(), 2)
    
    with self.assertRaises(Exception):
      test_list.add_first("asdf")

  def test_add_last(self):
    test_list = Linked_List()
    test_list.add_last(5)
    self.assertEqual(test_list.get_last(), 5)

    test_list2 = Linked_List()
    test_list2.add_last(2)
    self.assertEqual(test_list2.get_first(), 2)

    with self.assertRaises(Exception):
      test_list.add_last("asdf")

  def test_remove_last(self):
    test_list = Linked_List()
    test_list.add_last(6)
    test_list.add_last(7)
    self.assertEqual(test_list.remove_last(), 7)    

    with self.assertRaises(Exception):
      test_list2 = Linked_List()
      test_list2.get_last()
  
  def test_remove_first(self):
    test_list = Linked_List()
    test_list.add_last(5)
    test_list.add_last(6)
    self.assertEqual(test_list.remove_first(), 5)

    with self.assertRaises(Exception):
      test_list2 = Linked_List()
      test_list2.remove_first()
  
  def test_reverse(self): 
    test_list = Linked_List()
    test_list.add_last(1)
    test_list.add_last(2)
    test_list.add_last(3)
    test_list.add_last(4)

    test_list.reverse()
    self.assertEqual(test_list.get_first(), 4)
    self.assertEqual(test_list.get_last(), 1)
    self.assertEqual(test_list.__str__(), "4=>3=>2=>1")

if __name__ == '__main__':
  unittest.main()