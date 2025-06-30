from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        sortedCounts = sorted(counts.items(), key=lambda item: item[0])
        maxSum = -1
        if len(sortedCounts) < 2:
            return 0
        else:
            for i in range(len(sortedCounts) - 1):
                currentElement, currentCount = sortedCounts[i]

                nextElement, nextCount = sortedCounts[i + 1]

                currentSum = 0
                if abs(currentElement - nextElement) == 1:
                    currentSum = currentCount + nextCount

                if currentSum > maxSum:
                    maxSum = currentSum
                    elements_with_max_sum = (currentElement, nextElement)

        return maxSum

if __name__ == "__main__":
    nums = [1,3,2,2,5,2,3,7]
    sol = Solution()
    ans = sol.findLHS(nums)
    print(f"Answer: {ans}")
    nums = [1,1,1,1]
    ans = sol.findLHS(nums)
    print(f"Answer: {ans}")
    nums = [1,2,3,4]
    ans = sol.findLHS(nums)
    print(f"Answer: {ans}")
