import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        # Build a heap of size k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.heap, val)
        # If the heap exceeds size k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the root of the heap (k-th largest element)
        return self.heap[0]
