from Solution import Solution 
import functools

class PaintFence(Solution):

    def __init__(self):
        super().__init__()

    def solution(self, n: int, k: int) -> None:
        
        @functools.lru_cache(None)
        def dp(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            else:
                return (k - 1) * (dp(i - 1) + dp(i - 2))

        self.setSolution(dp(n))