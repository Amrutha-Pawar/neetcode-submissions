class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        
        if len(l1) != len(l2):
            return False

        if l1[0:] == l2[0:]:
            return True
        return False