from ds import Node1
# class Node:
#   def __init__(self, data=None, next=None):
#     self.data = data
#     self.next = next
class Data:
  def __init__(self, key, value):
    self.key = key
    self.value = value
class HashTable:
  def __init__(self, size):
    self.size = size
    self.hash_table = [None] * size
  
  def custom_hash(self, key):
    hashed_key = 0
    for i in key:
      hashed_key += ord(i)
      hashed_key = (hashed_key + ord(i)) % self.size
    return hashed_key
  
  def add_key_value(self, key, value):
    new_node = Node1(Data(key, value))
    hashed_key = self.custom_hash(key)
    if self.hash_table[hashed_key] is None:
      self.hash_table[hashed_key] = new_node
    else: # or use parallel arrays to keep track of each non empty cell's tail
      node = self.hash_table[hashed_key]
      while node.next:
        node = node.next
      self.hash_table[hashed_key].next = new_node

  def get_value(self, key):
    hashed_key = self.custom_hash(key)
    node = self.hash_table[hashed_key]
    while node:
      if node.data.key == key:
        return node.data.value
      node = node.next
    return node

  def __repr__(self):
    repr = "{\n"
    for i, node in enumerate(self.hash_table):
      repr += f"\t[{i}]"
      while node:
        repr += f" {node.data.key} : {node.data.value} ->"
        node = node.next
      repr += " None\n"
    repr += "}"
    return repr

# ht = HashTable(4)
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# print(ht)