from typing import List

'''
Idea:
Binary search through removable list for valid k cutoff.
Check validity with function that skips over "removed" letters and adds each time the appropriate letter is found.
If all appropriate letters are found, p_ptr == len(p) and subsequence is valid.
'''

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        self.s = s
        self.p = p
        self.removable = removable
        
        ans = 0
        low, high = 0, len(self.removable)

        while low <= high:
            k = (low + high) // 2
            if self._is_subsequence(k):
                ans = k
                low = k + 1
            else:
                high = k - 1
        
        return ans

    def _is_subsequence(self, k: int) -> bool:
        indices_to_remove = set(self.removable[:k])
        
        s_ptr = 0
        p_ptr = 0
        
        while s_ptr < len(self.s) and p_ptr < len(self.p):
            if s_ptr in indices_to_remove:
                s_ptr += 1
                continue
            
            if self.s[s_ptr] == self.p[p_ptr]:
                p_ptr += 1
            
            s_ptr += 1
            
        return p_ptr == len(self.p)

if __name__ == "__main__":
    s = "abcacb"
    p = "ab"
    removable = [3,1,0]
    sol = Solution()
    print(sol.maximumRemovals(s, p, removable))

    s = "abcddddd"
    p = "abcd"
    removable = [3,2,1,4,5,6]
    print(sol.maximumRemovals(s, p, removable))

