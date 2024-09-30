class Solution(object):
    def isSubsequence(self, s, t):
        i = 0  
        j = 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1  
            i += 1  

        
        return j == len(s)
