from ds import Node2

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def _insert_recursive(self, value, node):
    if value < node.data:
      if node.left is None:
        node.left = Node2(value)
      else:
        self._insert_recursive(value, node.left)
    elif value > node.data:
      if node.right is None:
        node.right = Node2(value)
      else:
        self._insert_recursive(value, node.right)
    else:
      return

  def insert(self, value):
    if self.root is None:
      self.root = Node2(value)
    else:
      self._insert_recursive(value, self.root)
  
  def inorder(self):
    if self.root:
      def _collect(node):
        left, val, right = [], [node.data], []
        if node.left:
          left = _collect(node.left)
        if node.right:
          right = _collect(node.right)
        return left + val + right
      
      return _collect(self.root)
    return None

  def levelOrder(self):
    if self.root is None:
      return None
    def TODO(arrq, values):
      if len(arrq) == 0:
        return values
      additions, count_deletions = [], len(arrq)
      for sub in arrq:
        values.append(sub.data)
        if sub.left:
          additions.append(sub.left)
        if sub.right:
          additions.append(sub.right)
      arrq = arrq[count_deletions:]
      arrq.extend(additions)
      return TODO(arrq, values)

    return TODO([self.root], [])

class BlogPostBST(BinarySearchTree):
  def _insert_recursive(self, data, node):
    if data["id"] < node.data["id"]:
      if node.left is None:
        node.left = Node2(data)
      else:
        self._insert_recursive(data, node.left)
    elif data["id"] > node.data["id"]:
      if node.right is None:
        node.right = Node2(data)
      else:
        self._insert_recursive(data, node.right)
    else:
      return
    
  def insert(self, data):
    if self.root is None:
      self.root = Node2(data)
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
# print(bst.inorder())
# bst.insert(20)
# bst.insert(1)
# bst.insert(2)
# bst.insert(30)
# print(bst.inorder())
# print(bst.levelOrder())

def isBinarySearchTree(tree):
  if (tree.root is None):
    return True

  def _isSubTree(node): #not node but tree
    if node is None:
      return True

    if node.left and node.right: # assuming not wrapper
      if node.left.data < node.data:
        if node.data < node.right.data:
          return _isSubTree(node.right) and _isSubTree(node.left)
        else:
          return False 
      else:
        return False

    if node.left:
      if node.left.data > node.data:
        return False
      else:
        return _isSubTree(node.left)
    if node.right:
      if node.right.data < node.data:
        return False
      else:
        return _isSubTree(node.right)
    
    return True
  return _isSubTree(tree.root)
# print(isBinarySearchTree(bst))

# fcc = BinarySearchTree()
# fcc.insert(7)
# fcc.insert(1)
# fcc.insert(9)
# fcc.insert(3)
# fcc.insert(5)
# fcc.insert(2)
# fcc.insert(0)
# fcc.insert(8)
# fcc.insert(10)
# print(fcc.levelOrder())
# print(fcc.inorder())
