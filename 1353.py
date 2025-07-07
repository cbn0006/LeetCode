from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort()

        # Initialize return result, heap, idx, and length
        result = 0
        heap = []
        idx = 0
        length = len(events)

        # Calculate absolute last day of going to an event
        lastDay = max(end for _, end in events)

        # For each day possible, see if you can go to an event
        for day in range(1, lastDay + 1):
            # Add event to heap if it is opening day for the event
            while idx < length and events[idx][0] == day:
                heapq.heappush(heap, events[idx][1])
                idx += 1
            
            # Remove ended events
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            # Pop the earliest event and add 1 to visited count
            if heap:
                heapq.heappop(heap)
                result += 1

            # If at the end and no more events to visit, stop looping
            if idx == length and not heap:
                break
        
        return result

            

if __name__ == "__main__":
    events = [[1,10],[2,2],[2,2],[2,2],[2,2]]
    sol = Solution()
    sol.maxEvents(events)

    # events = [[1,2], [2,3], [3,4], [1,2]]
    # sol.maxEvents(events)
    