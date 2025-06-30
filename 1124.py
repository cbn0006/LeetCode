from typing import List
# Longest Well-Performing Interval

# hours = list of num of hours worked per day for an employee
# tiring day = if hours > 8
# well-performing interval = interval of days where tiring > non-tiring days
# return the longest well-performing interval

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        begin = 0
        end = len(hours) - 1

        longestInterval = 0

        if max(hours) <= 8:
            return 0

        convertedList = ['y' if num > 8 else 'n' for num in hours]

        while begin != end:
            print(f"{convertedList[begin:end + 1].count('y')} : {convertedList[begin:end + 1].count('n')}")
            # If more tiring days than not in interval
            if convertedList[begin:end + 1].count('y') > (end + 1 - begin) / 2:
                length = end + 1 - begin
                if length > longestInterval:
                    longestInterval = length
            
            # If next slot from begin is non-tiring move
            if convertedList[begin + 1] == 'n':
                begin += 1
            elif convertedList[end - 1] == 'n':
                end -= 1
            else:
                begin += 1
        
        print(begin)
        if longestInterval == 0 and convertedList[begin] == 'y':
            return 1

        return longestInterval
    
if __name__ == "__main__":
    hours = [6,6,9]
    sol = Solution()
    ans = sol.longestWPI(hours)
    print(ans)
            