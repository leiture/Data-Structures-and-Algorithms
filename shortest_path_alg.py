# -*-coding:utf-8-*-

import json
import random


# matrix = [
#     [5, max, 10, max, 30, 100],
#     [max, max, 5, max, max, max],
#     [max, 15, max, 50, max, max],
#     [max, max, max, max, max, 10],
#     [max, max, max, 20, max, 60],
#     [max, 15, max, max, max, max],
# ]


class Matrix:
    """
    邻接矩阵 二维数组
    """

    def __init__(self, v, d, left=1, right=9, directed=False):
        """
        生成二维矩阵
        v:边数
        d:顶点数
        limit:权值最大值，最小值为0
        directed:有向图
        """
        if not isinstance(v, int) or not isinstance(d, int):
            raise Exception("v or d  not a INT")
        if not d > 0 or not v >= d:
            raise Exception("d is a -INT or v <= d")
        _max_ = float("inf")  # 正无穷大
        if directed:
            self.v = v if v < d * (d - 1) else d * (d - 1)
        else:
            self.v = v if v < d * (d - 1) // 2 else d * (d - 1) // 2
        self.d = d
        self.g = [[_max_ if j != i else 0 for j in range(d)] for i in range(d)]
        count = self.v
        while count:
            r, c = random.randint(0, d - 1), random.randint(0, d - 1)
            if self.g[r][c] == _max_:
                if directed:
                    self.g[r][c] = random.randint(left, right)
                else:
                    self.g[r][c] = self.g[c][r] = random.randint(left, right)
                count -= 1

    def __str__(self):
        s = "[\n"
        for v in self.g:
            s += "  " + json.dumps(v) + ",\n"
        s += "]"
        return s.replace("Infinity", "M")


def dijkstra(matrix, start):
    """
    desc:Dijkstra(迪杰斯特拉)算法是典型的单源最短路路径算法，⽤用于计算⼀
    一个节点到其他所有节点的最短路径。主要特点是以起始点为中⼼心向外
    层层扩展，直到扩展到终点为⽌。Dijkstra算法是很有代表性的最短路路径算法，
    注意该算法要求图中不存在负权边.
    matrix:邻接矩阵
    start:开始节点
    """
    # 保存经过的点
    passed = [start]
    # 保存为经过的点
    no_pass = [x for x in range(len(matrix)) if x != start]
    # 初始化start点到其他点的距离数组
    distance = matrix[start]
    # 遍历no_pass，找出其对应在distance中最小的值，将其从no_pass中放到passed中
    while no_pass:
        shortest_index = no_pass[0]
        # 获取到点start最近的点位置
        for index in no_pass:
            if distance[index] < distance[shortest_index]:
                shortest_index = index
        passed.append(shortest_index)
        no_pass.remove(shortest_index)
        # 更新distance
        for i in no_pass:
            distance[i] = min(distance[i], distance[shortest_index] + matrix[shortest_index][i])
    return distance


def floyd(matrix):
    """
    弗洛伊德算法：多源最短路径算法
    """
    n = len(matrix)
    # k: 中介点
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 取【Dis(i,k) + Dis(k,j)  Dis(i,j)】中的最小值更新dis(i,j)
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


if __name__ == '__main__':
    m = Matrix(4, 4, directed=False)
    print(m)
    # print(dijkstra(m.g, 0))
    floyd(m.g)
    print(m)
