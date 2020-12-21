# -*-coding:utf-8-*-
# author:Rayben
# desc:balance binary tree


class Tree(object):
    """
    balance binary tree(or avl tree):
        所有节点的左右子树的深度差的绝对值不超过1。
    """

    def __init__(self, v=None, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right
