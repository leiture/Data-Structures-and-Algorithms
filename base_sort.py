# -*-coding:utf-8-*-
# desc:classic sort alg
import random


class Sort:
    """
    Python classic sort alg
    """

    def bubble(self, lst, reverse=False):
        """
        bubble sort
        time complexity:O(n^2)
        space complexity:O(1)
        stability:stable
        """
        if not isinstance(lst, list):
            raise Exception("lst must be list type.")
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n):
                if (lst[j] > lst[i] and reverse) or (lst[j] < lst[i] and not reverse):
                    lst[j], lst[i] = lst[i], lst[j]
        return lst

    def select(self, lst, reverse=False):
        """
        select sort
        time complexity:O(n^2)
        space complexity:O(1)
        stability: not
        """
        if not isinstance(lst, list):
            raise Exception("lst must be list type.")
        n = len(lst)
        for i in range(n):
            max_or_min_index = i
            for j in range(i + 1, n):
                if (lst[j] > lst[max_or_min_index] and reverse) or (lst[j] < lst[max_or_min_index] and not reverse):
                    max_or_min_index = j
            if max_or_min_index != i:
                l[i], l[max_or_min_index] = l[max_or_min_index], l[i]
        return lst

    def insert(self, lst, reverse=False):
        """
        insert sort
        time complexity:O(n^2)
        space complexity:O(1)
        stability:stable
        """
        if not isinstance(lst, list):
            raise Exception("lst must be list type.")
        n = len(lst)
        for i in range(1, n):
            value = lst[i]
            position = i
            while position > 0 and [
                (l[position - 1] < value and reverse) or (l[position - 1] > value and not reverse)]:
                l[position] = l[position - 1]
                position -= 1
            l[position] = value
        return lst

    def shell(self, lst, reverse=False):
        """
        希尔排序
        time complexity:O(n*log(n))
        space complexity:O(1)
        stability:stable
        """
        n = len(lst)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                j = i
                while j >= gap:
                    if (lst[j - gap] < lst[j] and reverse) or (lst[j - gap] > lst[j] and not reverse):
                        lst[j - gap], lst[j] = lst[j], lst[j - gap]
                        j -= gap
                    else:
                        break
            gap = gap // 2
        return lst

    def merge(self, lst, reverse=False):
        """
        归并排序
        time complexity: O(n*log2 N)
        space complexity: O(n)
        stability:stable
        """
        n = len(lst)
        if n <= 1:
            return lst
        mid = n // 2
        left = self.merge(lst[0:mid], reverse)
        right = self.merge(lst[mid:], reverse)
        return self.__merge(left, right, reverse)

    @staticmethod
    def __merge(left, right, reverse=False):
        l = len(left)
        r = len(right)
        i = 0
        j = 0
        result = []
        while i < l and j < r:
            if (left[i] < right[j] and not reverse) or (left[i] > right[j] and reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def quick(self, lst, reverse=False):
        """
        快速排序
        time complexity:O(n*log2*N)
        space complexity:O(log2*N)
        stability:stable
        """
        n = len(lst)
        if n <= 1:
            return lst
        mid = 0
        left = list()
        right = list()
        for i in range(1, n):
            if lst[i] > lst[mid]:
                right.append(lst[i])
            else:
                left.append(lst[i])
        if reverse:
            return self.quick(right, reverse) + [lst[mid]] + self.quick(left, reverse)
        return self.quick(left, reverse) + [lst[mid]] + self.quick(right, reverse)


if __name__ == '__main__':
    l = [random.randint(0, 1000) for i in range(10)]
    print(l)
    # print(Sort().bubble(l, reverse=False))
    # print(Sort().select(l, reverse=True))
    # print(Sort().insert(l, reverse=False))
    # print(Sort().shell(l, reverse=True))
    # print(Sort().merge(l, reverse=False))
    print(Sort().quick(l, reverse=True))
    print(sorted(l, reverse=True))
