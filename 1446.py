class Solution:
    def maxPower(self, s: str) -> int:
        prevLetter = s[0]
        longest = 1
        currLength = 1
        for x in range(1, len(s)):
            if s[x] == prevLetter:
                currLength += 1
                if currLength > longest:
                    longest = currLength
            else:
                currLength = 1

            prevLetter = s[x]

        return longest

if __name__ == "__main__":
    s = "leetcode"
    sol = Solution()
    print(sol.maxPower(s))

    s = "abbcccddddeeeeedcba"
    print(sol.maxPower(s))