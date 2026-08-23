import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        minh = []
        for n, f in c.items():

            heapq.heappush(minh, (f, n))
            if len(minh)>k:
                heapq.heappop(minh)
        return [n for f, n in minh]
        