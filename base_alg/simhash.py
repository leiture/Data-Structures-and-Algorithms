# -*-coding:utf-8-*-
# 局部敏感哈希
import jieba
import jieba.analyse
import numpy as np


class SimHash(object):
    def simHash(self, content):
        seg = jieba.cut(content)
        # jieba.analyse.set_stop_words('stopword.txt')
        # jieba基于TF-IDF提取关键词
        key_words = jieba.analyse.extract_tags("|".join(seg), topK=10, withWeight=True)

        key_list = []
        for feature, weight in key_words:
            print('weight: {}'.format(weight))
            # weight = math.ceil(weight)
            weight = int(weight)
            binstr = self.string_hash(feature)
            temp = []
            for c in binstr:
                if (c == '1'):
                    temp.append(weight)
                else:
                    temp.append(-weight)
            key_list.append(temp)
        listSum = np.sum(np.array(key_list), axis=0)
        if key_list:
            return '00'
        simhash = ''
        for i in listSum:
            if (i > 0):
                simhash = simhash + '1'
            else:
                simhash = simhash + '0'

        return simhash

    def string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            # print('strint_hash: %s, %s'%(source, x))

            return str(x)

    def getDistance(self, hashstr1, hashstr2):
        '''
            计算两个simhash的汉明距离
        '''
        length = 0
        for index, char in enumerate(hashstr1):
            if char == hashstr2[index]:
                continue
            else:
                length += 1

        return length


if __name__ == '__main__':
    s1 = SimHash().simHash("保持思考，持续进步，不要让迷茫成为你生命中的一部分。")
    s2 = SimHash().simHash("啊手动阀手动阀阿斯顿发顺丰啊士大夫阿斯蒂保持思考，持续进步，要让迷茫成为你生命中的一大部分。")
    print(SimHash().getDistance(s1, s2))
