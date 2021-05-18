class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def _insert_recursive(self, value, node):
    if value < node.data:
      if node.left is None:
        node.left = Node(value)
      else:
        self._insert_recursive(value, node.left)
    elif value > node.data:
      if node.right is None:
        node.right = Node(value)
      else:
        self._insert_recursive(value, node.right)
    else:
      return

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      self._insert_recursive(value, self.root)

class BlogPostBST(BinarySearchTree):
  def _insert_recursive(self, data, node):
    if data["id"] < node.data["id"]:
      if node.left is None:
        node.left = Node(data)
      else:
        self._insert_recursive(data, node.left)
    elif data["id"] > node.data["id"]:
      if node.right is None:
        node.right = Node(data)
      else:
        self._insert_recursive(data, node.right)
    else:
      return
    
  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert_recursive(data, self.root)
  
  def search(self, blog_post_id):
    blog_post_id = int(blog_post_id)
    if self.root is None:
      return None
    else:
      return self._search_recursive(self.root, blog_post_id)

  def _search_recursive(self, node, blog_post_id):
    # if node.left is None and node.right is None:
    #   return False
    if blog_post_id == node.data["id"]:
      return node.data
    elif blog_post_id < node.data["id"] and node.left is not None:
      return self._search_recursive(node.left, blog_post_id)
    elif blog_post_id > node.data["id"] and node.right is not None:
      return self._search_recursive(node.right, blog_post_id)
    else:
      return None

# bst = BinarySearchTree()
# bst.insert(20)
# bst.insert(1)
# bst.insert(2)
# bst.insert(30)
