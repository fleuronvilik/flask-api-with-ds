from ds import Node1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, data):
    tail = Node1(data)
    if self.tail is None:
      self.head = self.tail = tail
    else:
      self.tail.next = tail
      self.tail = self.tail.next

  def dequeue(self):
    head = self.head
    if head:
      self.head = head.next
      if self.head is None:
        self.tail = None
      return head.data
    return None

# q = Queue()
# q.enqueue("du coiffeur")
# q.enqueue("à tropical sun")
# q.enqueue("à pied")
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())