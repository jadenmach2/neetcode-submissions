class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        visit = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    if (( r + dr) in range(rows) and (c + dc) in range(cols) and grid[r+dr][c+dc] == "1"  and ((r + dr, c + dc)) not in visit):
                        q.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))

            

            


        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        return island


        
        