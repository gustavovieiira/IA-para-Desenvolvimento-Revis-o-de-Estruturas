from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            best_profit = max(best_profit, price - min_price)

        return best_profit


if __name__ == "__main__":
    solution = Solution()
    print(solution.max_profit([7, 1, 5, 3, 6, 4]))
