from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))
