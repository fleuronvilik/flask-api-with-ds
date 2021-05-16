class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, data):
    new_head = Node(data, self.head)
    if self.head is None:
      self.tail = new_head
    self.head = new_head
  
  def append(self, data):
    if self.tail is None:
      self.add(data) # self.head = new_tail
    else:
      new_tail = Node(data)
      self.tail.next = new_tail
      self.tail = new_tail

  def __repr__(self):
    if self.head is None:
      return None
    llstr, node = "", self.head
    while node:
      llstr += f"{node.data} -> "
      node = node.next
    llstr += "None"
    return llstr

  def to_list(self):
    nodes = []
    node = self.head
    while node:
      nodes.append(node.data)
      node = node.next
    return nodes

  def get_user_by_id(self, user_id):
    node = self.head
    while node:
      if node.data["id"] == int(user_id):
        return node.data
      node = node.next
    return None

# ll = LinkedList()
# ll.add("data4")
# ll.add("data3")
# ll.add("data2")
# ll.add("data1")
# ll.append("data5")
# print(ll)
