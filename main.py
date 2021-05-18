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
  
  def add_first(self, e):
    if self.head == None:
      self.head = Node(e)
      return
    temp = Node(e, self.head)
    self.head = temp

  def add_last(self, e):
    if self.head == None:
      self.head = Node(e)
      return
    current = self.head
    while(current.next):
      current = current.next
    current.next = Node(e)

  def remove_last(self):
    current = self.head

    if current == None:
      return None
    if current.next == None:
      self.head == None
      return current.e
    
    while(current.next.next): 
      current = current.next
    last = current.next
    current.next = None
    return last.e

  def remove_first(self):
    if self.head == None:
      return None

    current = self.head
    self.head = current.next
    return current.e

  def get_first(self):
    if self.head:
      return self.head.e
    else:
      return None

  def get_last(self):
    current = self.head
    while current.next:
      current = current.next
    return current.e

  def show_list(self):
    current = self.head
    while current.next:
      print(f"{current.e}=>", end='')
      current = current.next
    print(current.e)

  def __str__(self):
    current = self.head
    return_string = str(current.e)
    while current.next:
      current = current.next
      return_string += ("=>" + str(current.e))
    return return_string
