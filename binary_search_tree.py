# -*-coding:utf:utf-8-*-
# desc:binary sort tree
import random


class Tree:
    """
    二叉排序树、二叉搜索树、二叉查找树
    对二叉查找树进⾏行行中序遍历，即可得到有序的数列列。
    """

    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right

    def insert(self, v, node):
        """
        插入
        :param node: instance of Tree
        :param v:
        :return:
        1) 若当前的⼆二叉查找树为空，则插⼊入的元素为根节点;
        2) 若插⼊入的元素值⼩小于根节点值，则将元素插⼊入到左⼦子树中;
        3) 若插⼊入的元素值不不⼩小于根节点值，则将元素插⼊入到右⼦子树中。
        """
        if node is None:
            return Tree(v)
        if node.value > v:
            node.left = self.insert(v, node.left)
        else:
            node.right = self.insert(v, node.right)
        return node

    def remove(self, v, node):
        """
        删除值为v的节点
        :param v:
        :param node:
        :return:
        """
        if node is None:
            return
        if node.value > v:
            node.left = self.remove(v, node.left)
        elif node.value < v:
            node.right = self.remove(v, node.right)
        else:
            if node.left and node.right:
                node.value = self.find_mix(node.right).value
                node.right = self.remove(node.value, node.right)
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                return
        return node

    def contains(self, t, root):
        """
        二叉树查找
        :param t:
        :param root:
        :return:
        """
        if not root:
            return False
        if t > root.value:
            return self.contains(t, root.right)
        elif t < root.value:
            return self.contains(t, root.left)
        else:
            return True

    def find_mix(self, root):
        """
        获取最小值的节点
        :param root:
        :return:
        """
        if not root:
            return
        if not root.left:
            return root
        return self.find_mix(root.left)

    def find_max(self, root):
        """
        获取值最大的节点
        :param root:
        :return:
        """
        if not root:
            return
        if not root.right:
            return root
        return self.find_max(root.right)


if __name__ == '__main__':
    n = Tree(55)
    for i in range(10):
        n = n.insert(random.randint(0, 100), n)
    n = n.insert(66, n)
    n = n.insert(65, n)
    n = n.insert(67, n)
    print(n.find_mix(n).value)
    print(n.find_max(n).value)
    n = n.remove(66, n)
    print(n)
