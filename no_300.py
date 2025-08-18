# LeetCode 300: Longest Increasing Subsequence
# Time: O(n log n), Space: O(n)

import bisect
from typing import List

class Solution300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

# ---------- Driver code ----------
if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    sol = Solution300()
    print("Output:", sol.lengthOfLIS(nums))  # Expected: 4