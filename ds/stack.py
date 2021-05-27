from ds import Node1

class Stack:
  def __init__(self):
    self.top = None
  def peek(self):
    if self.top:
      return self.top.data
  def push(self, data):
    next_node = self.top
    self.top = Node1(data, next_node)
  def pop(self):
    if self.top:
      removed = self.top
      self.top = self.top.next
      return removed.data

# p = Stack()
# p.push(2)
# p.push(3)
# p.push(5)
# p.push(7)
# p.push(11)

# print(p.pop())
# print(p.pop())
# print(p.pop())
# print(p.pop())
# print(p.pop())
# print(p.pop())