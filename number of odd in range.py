class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0:
            return (high-low+1)//2
        return (high-low)//2 + 1







# print(Solution.countOdds(Solution, 3,7))






