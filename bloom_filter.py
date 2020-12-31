# -*-coding:utf-8-*-
import random

import mmh3
from bitarray import bitarray


class BloomFilter:
    """
    布隆过滤器
    """

    def __init__(self, size=800000, hashes=6):
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
    for _ in range(400000):
        bf.add(str(random.randint(-999999999, 999999999)))
    bf.contains("raybenleiture")
