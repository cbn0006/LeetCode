from typing import List

'''
Three cases:
Odd + Odd = Even
Even + Even = Even
Even + Odd = Odd

Logic:
Find first odd and check odd + odd subsequence length and odd + even subsequence length.
Find first even and check even + even subsequence length and even + odd length.

Theoretical Time Complexity:
O(4n)
'''

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        firstEvenPos = None
        firstOddPos = None
        longest = 0
        i = 0
        # Find first even
        while not firstEvenPos:
            if i == len(nums):
                i = 0
                break
            if nums[i] % 2 == 0:
                firstEvenPos = i
                i = 0
                break
            else:
                i += 1

        # Find first odd
        while not firstOddPos:
            if i == len(nums):
                break
            if nums[i] % 2 == 1:
                firstOddPos = i
                i = 0
                break
            else:
                i += 1
        
        # print(f'After setting positions: \nOdd Pos: {firstOddPos}\nEven Pos: {firstEvenPos}')

        # Evens loop
        if isinstance(firstEvenPos, int):
            for a in range(0,2):
                lengthEvens = 1 
                firstNum = nums[firstEvenPos]
                for x in range(firstEvenPos + 1, len(nums)):
                    secondNum = nums[x]
                    if (firstNum + secondNum) % 2 == a:
                        lengthEvens += 1
                        firstNum = secondNum
                    else:
                        continue
                print(f'Length Evens after loop {a}: {lengthEvens}')
                if lengthEvens > longest:
                    longest = lengthEvens
                    
        # Odds loop
        if isinstance(firstOddPos, int):
            for b in range(0,2):
                lengthOdds = 1
                firstNum = nums[firstOddPos]
                for y in range(firstOddPos + 1, len(nums)):
                    secondNum = nums[y]
                    if (firstNum + secondNum) % 2 == b:
                        lengthOdds += 1
                        firstNum = secondNum
                    else:
                        continue
                print(f'Length Odds after loop {b}: {lengthOdds}')
                if lengthOdds > longest:
                    longest = lengthOdds

        print(f'Longest subsequence: {longest}')
        return longest
                
if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()  
    sol.maximumLength(nums)

    nums = [1,2,1,1,2,1,2]
    sol.maximumLength(nums)

    nums = [1,3]
    sol.maximumLength(nums)