"""
URL: https://leetcode.com/problems/can-make-palindrome-from-substring/
"""
from typing import List


class Solution:

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        answer = []

        # make a list of count to store all the occurrences of alphabet up to that index in the string
        count_till_index = []
        previous_index = -1
        for index, letter in enumerate(s):
            if previous_index == -1:
                previous_count = {}
            else:
                previous_count = count_till_index[index-1]
            new_count = {**previous_count}
            if letter not in previous_count:
                new_count[letter] = 1
            else:
                new_count[letter] = previous_count[letter] + 1
            previous_index = index
            count_till_index.append(new_count)

        for query in queries:
            if query[0] == query[1]:
                answer.append(True)
                continue

            first_count_till_index = count_till_index[query[0] - 1] if query[0] != 0 else {}
            last_count_till_index = count_till_index[query[1]]
            substring_count = {}
            for char in last_count_till_index.keys():
                count_for_char = last_count_till_index[char] - first_count_till_index[char] if char in first_count_till_index else last_count_till_index[char]
                substring_count[char] = count_for_char

            max_odd_frequency = (query[2] * 2) + 1
            num_odds = 0
            for char, count in substring_count.items():
                if count % 2 != 0:
                    num_odds += 1
            answer.append(False if num_odds > max_odd_frequency else True)
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
