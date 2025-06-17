class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if n > (k * 2) + (m - k):
            return 0



if __name__ == "__main__":
    sol = Solution()
    n = 3
    m = 2
    k = 1
    sol.countGoodArrays(n,m,k)
