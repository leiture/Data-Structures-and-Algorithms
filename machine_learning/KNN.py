# -*-coding:utf-8-*-
# /usr/bin/python3
__author__ = "RayBen"

import operator

import numpy as np

"""
k近邻算法:物以类聚的惰性算法。KNN
模型：训练集+距离度量+K值+分类决策规则。
    距离度量：欧式距离、曼哈顿距离、切比雪夫距离、夹角余弦
    K值：越小==>近似误差变小，估计误差变大；易过拟合，模型变得复杂。
    近似误差：对现有训练据训练的训练误差。模型估计值与实际值的误差。
    估计误差：对现有测试集测试的测试误差。模型估计系数和实际系数之间的误差。
    分类决策规则：确定分类的标准。如多数服从少数，达到限定阈值等。
    
优势：简单、易于理解、容易实现、无需估计参数、无需训练（重要）
     模型构造简单。
     适用于解决稀有事件分类问题。（构造客户流失预测模型）
     适用用解决多分类问题。如根据基因特征判断其功能分类。
劣势：惰性算法，预测时才计算，计算量大，内存开销大，评分慢。
     对样本敏感，当样本中某一类别占有率高时，可能导致输入样本错误分类。
     可解释性差。
     
     
步骤如下：
1)根据给定的距离度量量，在训练集 中找出与 最邻近的 个点，涵盖这k个点的 领域记作 ; 
2)在 中根据分类决策规则（如多数表决）决定 的类别 :
        y = arg max ∑I( Y= X  ,  i = 1,2,···,N;j = 1,2,···,K 
其中 为指示函数，即Y当X 时为1，否则为0.
"""


class KNNClassifier:
    """
    k近岭回归算法
    """

    def __init__(self, k=3):
        self._k = k

    @staticmethod
    def _cal_distance(input_x, train_x):
        """
        计算输入x与样本中各点距离.
        """
        train_size = train_x.shape[0]
        diff_x = np.tile(input_x, (train_size, 1)) - train_x
        # 计算输入点到每个样本的距离
        # 欧式距离
        distance = (diff_x ** 2).sum(axis=1) ** 0.5
        # 曼哈顿距离
        # distance = np.abs(diff_x).sum(axis=1)
        # 对dintance排序，返回从小到大的索引数组
        sorted_indices = distance.argsort()
        return sorted_indices

    def _classify(self, input_x, train_x, train_y):
        sorted_indices = self._cal_distance(input_x, train_x)
        count_d = {}
        for i in range(self._k):
            label = train_y[sorted_indices[i]]
            count_d[label] = count_d.get(label, 0) + 1
        sorted_d = sorted(count_d.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_d[0][0]

    def classify(self, input_x, train_x, train_y):
        # 校验
        if isinstance(input_x, np.ndarray) and isinstance(train_x, np.ndarray) and isinstance(train_y, np.ndarray):
            pass
        else:
            try:
                input_x = np.array(input_x)
                train_x = np.array(train_x)
                train_y = np.array(train_y)
            except Exception:
                raise TypeError("numpy.ndarray is required for input_x、train_x and train_y")
        nd = len(np.shape(input_x))
        results = []
        if nd == 1:
            results.append(self._classify(input_x, train_x, train_y))
        else:
            for x in input_x:
                results.append(self._classify(x, train_x, train_y))
        return results


if __name__ == '__main__':
    trainX = [[1, 1.1], [1, 1], [0, 0], [0, 0.1]]
    trainY = ['A', 'A', 'B', 'B']
    clf = KNNClassifier(k=3)
    inputX = [[0, 0.1], [0.5, 0]]
    result = clf.classify(inputX, trainX, trainY)
    print(result)
