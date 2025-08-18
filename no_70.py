# LeetCode 70: Climbing Stairs
# Time: O(n), Space: O(1)

class Solution70:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second

# ---------- Driver code ----------
if __name__ == "__main__":
    n = 5
    sol = Solution70()
    print("Output:", sol.climbStairs(n))  # Expected: 8
