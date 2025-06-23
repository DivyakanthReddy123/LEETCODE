class Solution(object):
    def maxSubArray(self, nums):
        # when sum goes negative .. then start from 0 and keep on comparing with 
        # previous max val 

        if len(nums) == 1 :
            return nums[0]

        currSum = 0 
        maxSum = float('-inf')

        for num in nums :
            # currSum += num # this line should be below the if statement 
            # because , then we get the true max subarry 
            if currSum < 0 :
                currSum = 0
            currSum += num 
            maxSum = max (maxSum , currSum)

        return maxSum 