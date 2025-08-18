# LeetCode 198: House Robber
# Time: O(n), Space: O(1)

from typing import List

class Solution198:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1

# ---------- Driver code ----------
if __name__ == "__main__":
    nums = [2,7,9,3,1]
    sol = Solution198()
    print("Output:", sol.rob(nums))  # Expected: 12