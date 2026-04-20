class Solution(object):
    def maxDistance(self, nums1, nums2):
        i = 0 
        j = 0
        maxdis = 0
        while i <= len(nums1)-1 and j <= len(nums2)-1:
        
            if nums1[i] <= nums2[j] : 
                if j-i > maxdis :
                    maxdis = j-i
                j += 1
            else :
                i += 1
            print(maxdis)
        return maxdis
