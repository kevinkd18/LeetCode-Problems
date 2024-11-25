from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = 2, 3
        goal = "123450"
        start = ''.join(str(board[i][j]) for i in range(m) for j in range(n))

        if start == goal:
            return 0

        queue = deque([start])
        seen = {start}
        step = 0

        while queue:
            step += 1
            for _ in range(len(queue)):
                s = queue.popleft()
                zeroIndex = s.index('0')
                i, j = divmod(zeroIndex, n)
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        swappedIndex = x * n + y
                        # Create a new state by swapping
                        new_s = list(s)
                        new_s[zeroIndex], new_s[swappedIndex] = new_s[swappedIndex], new_s[zeroIndex]
                        new_s = ''.join(new_s)
                        if new_s == goal:
                            return step
                        if new_s not in seen:
                            queue.append(new_s)
                            seen.add(new_s)

        return -1
