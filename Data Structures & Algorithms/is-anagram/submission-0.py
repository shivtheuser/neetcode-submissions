class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        if len(s) != len(t):
            return False
        for i in s:
            mp1[i] = mp1.get(i,0)+1
        for i in t:
            mp1[i] = mp1.get(i,0)-1
            if mp1[i] == 0:
                del mp1[i]
        if not mp1:
            return True
        else:
            return False
        