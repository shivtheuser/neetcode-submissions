class Solution:
    def XORtillN(self,n):
        if n%4 == 0:
            return n
        elif n%4 == 1:
            return 1
        elif n%4 == 2:
            return n+1
        else:
            return 0
            
    def findXOR(self, l, r):
        # code here
        return self.XORtillN(r) ^ self.XORtillN(l-1)
