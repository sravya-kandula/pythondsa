# LeetCode 33: Search in Rotated Sorted Array
# Time: O(log n), Space: O(1)

from typing import List

class Solution33:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# ---------- Driver code ----------
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution33()
    print("Output:", sol.search(nums, target))  # Expected: 4