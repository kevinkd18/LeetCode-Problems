from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),   # horizontal & vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1) # diagonal
        ]
        
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # mark start as visited
        
        while queue:
            x, y, path_length = queue.popleft()
            
            if x == n - 1 and y == n - 1:  # reached bottom-right corner
                return path_length
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    queue.append((nx, ny, path_length + 1))
                    grid[nx][ny] = 1  # mark as visited
        
        return -1
