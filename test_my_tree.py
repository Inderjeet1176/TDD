import unittest
from my_tree import MyTree

class TestMyTree(unittest.TestCase):
    def test_new_tree_is_empty(self):
        tree = MyTree()
        self.assertTrue(tree.is_empty())  


