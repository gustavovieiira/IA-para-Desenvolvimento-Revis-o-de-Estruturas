from typing import List


class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_index = stack.pop()
                answer[previous_index] = index - previous_index

            stack.append(index)

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
