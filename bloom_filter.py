# -*-coding:utf-8-*-
import random
import string

import mmh3
from bitarray import bitarray


class BloomFilter:
    """
    布隆过滤器
    """

    def __init__(self, size=100000, hashes=4):
        """
        size:比特数组长度
        hashes:哈希函数个数（murmurhash3）
        """
        self.size = size
        self.hashes = hashes
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, _str):
        """
        在比特数组中添加_str指纹
        """
        fingers = self.get_finger_print(_str)
        for b in fingers:
            self.bit_array[b] = 1

    def get_finger_print(self, _str):
        """
        使用murmurHash3哈希算法
        """
        return [mmh3.hash(_str, 256 + i) % self.size for i in range(self.hashes)]

    def contains(self, _str):
        """
        查询_str是否存在比特数组中
        """
        fingers = self.get_finger_print(_str)
        return all(map(lambda b: self.bit_array[b] == 1, fingers))


if __name__ == '__main__':
    bf = BloomFilter()
    occupancy = 10000
    count = 0
    _str = None
    for _ in range(100):
        for _ in range(occupancy):
            bf.add(str(random.randint(-999999999, 999999999)))
        _str = "".join([random.choice(string.printable) for _ in range(100)])
        if not bf.contains(_str):
            count += 1
    print(bf.get_finger_print(_str))
    print("occupancy rate:", occupancy / bf.size)
    print("correct rate:", count / 100)
