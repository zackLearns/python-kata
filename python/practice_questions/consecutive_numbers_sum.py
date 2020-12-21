"""
URL: https://leetcode.com/problems/consecutive-numbers-sum/
"""
from math import ceil


class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        upper_limit = ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(f'Should print 2: {solution.consecutiveNumbersSum(5)}')
    print(f'Should print 3: {solution.consecutiveNumbersSum(9)}')
    print(f'Should print 4: {solution.consecutiveNumbersSum(15)}')
