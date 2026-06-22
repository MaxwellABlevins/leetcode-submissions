class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False

        for v in s:
            if s.count(v) != t.count(v):
                return False
            
        return True