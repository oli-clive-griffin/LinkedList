class Node:
  def __init__(self, e, next=None):
    self.e = e
    self.next = next


class Linked_List:
  def __init__(self, e=None):
    if e == None:
      self.head = None
    else:
      self.head = Node(e)
  
  # time complexity: O(1)
  def add_first(self, e):
    if not isinstance(e, int):
      raise Exception("wrong data type")

    self.head = Node(e, self.head)

  # time complexity: O(n)
  def add_last(self, e):
    if not isinstance(e, int):
      raise Exception("wrong data type")

    current = self.head
    if current == None:
      self.head = Node(e)
    else:
      while(current.next):
        current = current.next
      current.next = Node(e)

  # time complexity: O(1)
  def remove_first(self):
    current = self.head
    if current == None:
      raise Exception("list is empty")

    self.head = current.next
    return current.e

  # time complexity: O(n)
  def remove_last(self):
    current = self.head
    if current == None:
      raise Exception("list is empty")
    if current.next == None:
      self.head = None
      return current.e

    while(current.next.next): 
      current = current.next
    last = current.next
    current.next = None
    return last.e

  # time complexity: O(1)
  def get_first(self):
    return self.head.e if self.head else None

  # time complexity: O(n)
  def get_last(self):
    current = self.head
    while current.next:
      current = current.next
    return current.e

  # time complexity: O(n)
  def show_list(self):
    if self.head == None:
      return None
      
    current = self.head
    print(current.e, end='')
    while current.next:
      current = current.next
      print(f"=>{current.e}", end='')

  # time complexity: O(n)
  # basically just a python version of show_list
  def __str__(self):
    if self.head == None:
      return None

    current = self.head
    return_string = str(current.e)
    while current.next:
      current = current.next
      return_string += (f"=>{current.e}")
    return return_string

  # time complexity: O(n)
  def reverse(self):
    if self.head == None:
      raise Exception("list is empty")
    if self.head.next == None:
      raise Exception("list only has one element")

    previous = None
    current = self.head
    while (current is not None):
      nxt = current.next
      current.next = previous
      previous = current 
      current = nxt
    self.head = previous