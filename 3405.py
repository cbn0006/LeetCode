class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        d = n - 1
        if k > d:
            return 0
        r = k
        C = 1
        if r > d - r:
            r = d - r
        
        if r:
            inv = [0] * (r + 1)
            inv[1] = 1
            for i in range(2, r + 1):
                inv[i] = mod - (mod // i) * inv[mod % i] % mod
            for i in range(1, r + 1):
                C = C * (d - r + i) % mod * inv[i] % mod
        return m * C % mod * pow(m - 1, d - k, mod) % mod
        



if __name__ == "__main__":
    sol = Solution()
    n = 3
    m = 2
    k = 1
    answer = sol.countGoodArrays(n,m,k)
    print(answer)



# Python3 Solutions:
'''
One-liner:
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m*pow(m-1, n-k-1, mod:=10**9+7)*comb(n-1, k)%mod


'''
