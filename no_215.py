# LeetCode 215: Kth Largest Element in an Array
# Time: O(n log k), Space: O(k)

import heapq
from typing import List

class Solution215:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# ---------- Driver code ----------
if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution215()
    print("Output:", sol.findKthLargest(nums, k))  # Expected: 5
