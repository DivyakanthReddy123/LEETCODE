class Solution(object):
    def snakesAndLadders(self, board):
        from collections import deque
        n = len(board)
        target = n * n                       # last square number
        
        # ---------- helper: map 1-based square -> (row, col) ----------
        def square_to_rc(sq):
            """Return (row, col) on the board for a given square number (1-based)."""
            sq -= 1                         # 0-based index
            r = n - 1 - (sq // n)           # rows counted from bottom
            c = sq % n
            if ((n - 1 - r) % 2) == 1:      # odd row from bottom → reversed
                c = n - 1 - c
            return r, c
        
        # ---------- BFS ----------
        q = deque([(1, 0)])                 # (square, rolls)
        seen = {1}
        
        while q:
            square, rolls = q.popleft()
            if square == target:
                return rolls
            for step in range(1, 7):        # die roll 1‒6
                nxt = square + step
                if nxt > target:
                    break
                r, c = square_to_rc(nxt)
                if board[r][c] != -1:       # snake or ladder
                    nxt = board[r][c]
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, rolls + 1))
        
        return -1                           # unreachable   
        