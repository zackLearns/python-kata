"""
URL: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
"""
from typing import List
import heapq


class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        res, d = 0, events[0][0]
        heap = []
        while events or heap:
            # Add new events that can be attended on day `d`
            while len(events) > 0 and events[0][0] == d:
                heapq.heappush(heap, events.pop(0)[1])

            # remove events that are already completed
            while heap and heap[0] < d:
                heapq.heappop(heap)

            # attend one event in day `d`
            if len(heap) > 0:
                res += 1
                heapq.heappop(heap)

            d += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(f'Should be 3: {solution.maxEvents([[1, 2], [2, 3], [3, 4]])}')
    print(f'Should be 4: {solution.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]])}')
    print(f'Should be 4: {solution.maxEvents([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]])}')
    print(f'Should be 1: {solution.maxEvents([[1, 100000]])}')
    print(f'Should be 7: {solution.maxEvents([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]])}')
    print(f'Should be 5: {solution.maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]])}')
    print(f'Should be 4: {solution.maxEvents([[1, 3], [1, 3], [1, 3], [3, 4]])}')
