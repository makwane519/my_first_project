class Solution:
    def wifiRange(self, s, x):
        n = len(s)

        # Array to track coverage
        covered = [0] * n

        for i in range(n):
            if s[i] == '1':
                left = max(0, i - x)
                right = min(n - 1, i + x)
                # Mark all rooms from left → right as covered
                for j in range(left, right + 1):
                    covered[j] = 1

        # If any room is not covered, return False
        return all(covered)