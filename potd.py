class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        last_covered = -1  # last room that is covered

        for i in range(n):
            if s[i] == '1':
                left = i - x
                right = i + x

                # If there exists an uncovered gap between last_covered+1 and left-1
                if left > last_covered + 1:
                    return False

                # Extend coverage to right
                last_covered = right

        # After loop, ensure the last room is covered
        return last_covered >= n - 1