# logic 

# we store the current num with its idx 
# and we keep on finding the complement for every number we visit 
# and we check the complement in the dictionary , if we find it means
# that we already have the complement and its index , and now we
# we also have the current number's index 
# so we print both the values in an array 


# Time Complexity -> O(N) size of nums array 
# Space Complexity -> O(N) bc of the dictionary 
class Solution(object):
    def twoSum(self, nums, target):
        complements = {}
        for idx , num in enumerate(nums):
            complement = target - num
            if complement in complements :
                return [complements[complement],idx]
            else :
                complements[num] = idx 

        