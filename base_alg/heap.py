# -*-coding:utf-8-*-
import math


class Heap:

    def __init__(self, lst):
        if isinstance(lst, list):
            self.h = lst

    def heap_adjust(self, index):
        """
        堆排序
        """
        n = len(self.h)
        left = self.left_c(index)
        while left < n and index < n:
            # 比较左右子树的值
            if left + 1 < n and self.h[left] < self.h[left + 1]:
                left += 1
            # 比较最大子树值与父节点的值
            if self.h[index] < self.h[left]:
                self.h[index], self.h[left] = self.h[left], self.h[index]
            else:
                break
            index = left
            left = self.left_c(index)

    def sort(self):
        n = len(self.h)
        for index in range(n // 2 - 1, -1, -1):
            self.heap_adjust(index)
        print(self.h)
        for index in range(n - 1, -1, -1):
            self.h[0], self.h[index] = self.h[index], self.h[0]
            self.heap_adjust(index)

    @staticmethod
    def left_c(index):
        """
        left child
        """
        return index * 2 + 1

    def right_c(self, index):
        return self.left_c(index) + 1

    @staticmethod
    def present(index):
        """
        节点index的父节点 在[0,len(self.h))
        根节点没有父节点
        """
        return math.floor(index / 2)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    h = Heap(l)
    h.sort()
    print(h.h)
