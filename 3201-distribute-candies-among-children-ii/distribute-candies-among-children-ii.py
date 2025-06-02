


import math

class Solution(object):
    def distributeCandies(self, n, limit):
        def ways(m) :
            return 0 if m < 0 else (m + 2) * (m + 1) // 2

        L = limit + 1
        return ( ways(n)
               - 3 * ways(n - L)
               + 3 * ways(n - 2 * L)
               -     ways(n - 3 * L) )