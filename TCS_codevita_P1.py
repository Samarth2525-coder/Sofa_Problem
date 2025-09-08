from collections import deque

def is_free(grid, x, y, M, N):
    return 0 <= x < M and 0 <= y < N and grid[x][y] != "H"

def sofa_problem(M, N, grid):
    # Find start and target sofa positions
    start, target = None, None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "s":
                if start is None:
                    start = (i, j)
                else:
                    # orientation from two 's'
                    if start[0] == i:
                        start_state = (i, min(j, start[1]), "H")
                    else:
                        start_state = (min(i, start[0]), j, "V")
            if grid[i][j] == "S":
                if target is None:
                    target = (i, j)
                else:
                    if target[0] == i:
                        target_state = (i, min(j, target[1]), "H")
                    else:
                        target_state = (min(i, target[0]), j, "V")

    # BFS
    q = deque([(start_state, 0)])
    visited = set([start_state])

    while q:
        (x, y, o), steps = q.popleft()

        # Goal check
        if (x, y, o) == target_state:
            return steps

        if o == "H":  # sofa occupies (x,y) and (x,y+1)
            # Move left
            if y > 0 and is_free(grid, x, y-1, M, N) and is_free(grid, x, y, M, N):
                nxt = (x, y-1, "H")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Move right
            if y+2 < N and is_free(grid, x, y+2, M, N):
                nxt = (x, y+1, "H")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Move up
            if x > 0 and is_free(grid, x-1, y, M, N) and is_free(grid, x-1, y+1, M, N):
                nxt = (x-1, y, "H")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Move down
            if x+1 < M and is_free(grid, x+1, y, M, N) and is_free(grid, x+1, y+1, M, N):
                nxt = (x+1, y, "H")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Rotate (needs 2x2 free block)
            if x+1 < M and is_free(grid, x, y, M, N) and is_free(grid, x, y+1, M, N) and is_free(grid, x+1, y, M, N) and is_free(grid, x+1, y+1, M, N):
                for nxt in [(x, y, "V"), (x, y+1, "V")]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps+1))

        else:  # Vertical: sofa occupies (x,y) and (x+1,y)
            # Move up
            if x > 0 and is_free(grid, x-1, y, M, N):
                nxt = (x-1, y, "V")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Move down
            if x+2 < M and is_free(grid, x+2, y, M, N):
                nxt = (x+1, y, "V")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Move left
            if y > 0 and is_free(grid, x, y-1, M, N) and is_free(grid, x+1, y-1, M, N):
                nxt = (x, y-1, "V")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Move right
            if y+1 < N and is_free(grid, x, y+1, M, N) and is_free(grid, x+1, y+1, M, N):
                nxt = (x, y+1, "V")
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
            # Rotate
            if y+1 < N and is_free(grid, x, y, M, N) and is_free(grid, x+1, y, M, N) and is_free(grid, x, y+1, M, N) and is_free(grid, x+1, y+1, M, N):
                for nxt in [(x, y, "H"), (x+1, y, "H")]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps+1))

    return "Impossible"


# -------- DRIVER --------
if __name__ == "__main__":
    M, N = map(int, input().split())
    grid = [input().split() for _ in range(M)]
    print(sofa_problem(M, N, grid))
