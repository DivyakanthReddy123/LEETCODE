# TC O(N) , SC O(N)
# LOGIC 

# two local comparisons are enough , child only compares with its immediate neighbour 

# we move from LEFT to RIGHT and then RIGHT to LEFT so that in both the directions the inequality is satisfied .

# why use MAX ?? -> 
# example -> ratings = [1, 3, 4, 5, 2]
# after L to R -> Candies so far: [1, 2, 3, 4, 1]
# Now the R→L pass hits index 3:
#ratings[3] = 5 > ratings[4] = 2 → need at least candies[4] + 1 = 2.
# candies[3] is already 4.
# max(4, 2) = 4, so we keep the larger value.



class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n                    # baseline
        
        # left → right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # right → left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
        
