class Solution(object):
    def minimumDistance(self, nums):
        s = { }

        if len(nums) < 3 :
            return -1

        for i in range(len(nums)) : 
            if nums[i] in s : 
                s[nums[i]].append(i)
            else : 
                s[nums[i]] = [i]

        print(s)
        n = {}
        m = float("inf")
        for e in s :
            if len(s[e]) >= 3 :
                for x in range(len(s[e])-2) :    
                    i = s[e][x]
                    j = s[e][x+1]
                    k = s[e][x+2]
                    val = abs(i - j) + abs(j - k) + abs(k - i)
                    print(val)
                    print(m)
                    if val < m : 
                        m = val 


            
        if m == float("inf") :
            return -1 
        else : 
            return m


        