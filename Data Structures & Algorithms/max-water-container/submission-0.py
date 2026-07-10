class Solution:
    def maxArea(self, h: List[int]) -> int:
        x, y = 0, len(h) - 1
        a = 0
        while x < y:
            a = max(a, min(h[x], h[y])*(y-x))
            if h[x] < h[y]:
                x += 1
            else:
                y -= 1
        return a
