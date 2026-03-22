class Solution(object):
    def lengthOfLastWord(self, s):
        rev = s[::-1]
        c = 0 
        print(rev)
        for i in rev : 
            if i == " " and c == 0 : 
                continue
            elif i == " " and c >= 1:
                return  c    
            else : 
                print(i)
                c+= 1 

        return c
        