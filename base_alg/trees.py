class Node:
    """
    二叉树类
    """

    def __init__(self, v=None):
        self.value = v
        self.left = None
        self.right = None
        self.h = 0


def pre_order(root: Node):
    """
    递归实现
    前序遍历二叉树   根节点-->左子树-->右子树
    :param root:
    :return:
    """
    if not root:
        return
    print(root.value, end=",")
    pre_order(root.left)
    pre_order(root.right)


def pre_order_(root: Node):
    """
    非递归实现
    前序遍历二叉树   根节点-->左子树-->右子树
    :param root:
    :return:
    """
    l = list()
    while root or l:
        while root:
            print(root.value, end=",")
            l.append(root)
            root = root.left
        root = l.pop(-1)
        root = root.right
    print()


def pre_order_1(root: Node):
    """
    非递归实现
    前序遍历二叉树   根节点-->左子树-->右子树
    :param root:
    :return:
    """
    l = list()
    l.append(root)
    while l:
        cur = l.pop()
        print(cur.value, end=",")
        l.append(cur.right) if cur.right else None
        l.append(cur.left) if cur.left else None
    print()


def mid_order(root: Node):
    """
    递归实现
    中序遍历二叉树   左子树-->根节点-->右子树
    :param node:
    :return:
    """
    if root:
        mid_order(root.left)
        print(root.value, end=",")
        mid_order(root.right)


def mid_order_(root: Node):
    """
    非递归实现
    中序遍历二叉树   左子树-->根节点-->右子树
    :param node:
    :return:
    """
    l = list()
    while root or l:
        while root:
            l.append(root)
            root = root.left
        root = l.pop()
        print(root.value, end=",")
        root = root.right


def last_order(root: Node):
    """
    递归
    后序遍历二叉树   左子树 ---> 右子树 ---> 根结点
    :param root:
    :return:
    """
    if root:
        last_order(root.left)
        last_order(root.right)
        print(root.value, end=",")


def last_order_(root: Node):
    """
    非递归
    后序遍历二叉树   左子树 ---> 右子树 ---> 根结点
    :param root:
    :return:
    """
    l1 = list()
    l2 = list()
    while l1:
        node = l1.pop()
        l1.append(node.left) if node.left else None
        l1.append(node.right) if node.right else None
        l2.append(node)
    while l2:
        node = l2.pop()
        print(node.value, end=",")


def level_order(root: Node):
    """
    层序遍历
    只需按层次遍历即可
    :param root:
    :return:
    """
    l = list()
    l.append(root)
    while l:
        node = l.pop(0)
        print(node.value, end=",")
        l.append(node.left) if node.left else None
        l.append(node.right) if node.right else None


def make_node(l=3, s=0):
    """
    生成树
    节点数 2**(l+1)-1
    :param l:
    :return:
    """
    if not s:
        s = l + 1
    n = Node()
    n.value = s - l
    n.h = l + 1
    if not l:
        return n
    n.left = make_node(l - 1, s)
    n.right = make_node(l - 1
                        , s + 1)
    return n


if __name__ == '__main__':
    s = make_node(2)
    pre_order(s)
    print()
    mid_order(s)
    print()
    last_order(s)
    print()
    level_order(s)
