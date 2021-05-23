"""
URL: https://leetcode.com/problems/range-sum-query-2d-immutable/
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        origin_sum = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row_index, row_values in enumerate(matrix):
            for col_index, value in enumerate(row_values):
                if row_index == 0 and col_index == 0:
                    origin_sum[row_index][col_index] = value
                elif row_index == 0:
                    origin_sum[row_index][col_index] = origin_sum[row_index][col_index - 1] + value
                elif col_index == 0:
                    origin_sum[row_index][col_index] = origin_sum[row_index - 1][col_index] + value
                else:
                    origin_sum[row_index][col_index] = value + origin_sum[row_index][col_index - 1] + origin_sum[row_index - 1][col_index] - origin_sum[row_index - 1][col_index - 1]
        self.origin_sum = origin_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = self.origin_sum[row2][col2]
        if row2 >= 0 and col1 >= 1:
            sum_region -= self.origin_sum[row2][col1-1]
        if col2 >= 0 and row1 >= 1:
            sum_region -= self.origin_sum[row1-1][col2]
        if row1 >= 1 and col1 >= 1:
            sum_region += self.origin_sum[row1-1][col1-1]

        return sum_region


if __name__ == '__main__':
    # Your NumMatrix object will be instantiated and called as such:
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(2, 1, 4, 3)
    # param_1 = obj.sumRegion(0, 0, 0, 0)
    # param_1 = obj.sumRegion(0, 0, 0, 1)
    param_1 = obj.sumRegion(1, 0, 2, 2)
    print(param_1)

