class Solution:
    def checkKthBit(self, n, k):
        # code here
        ##left shift
        
        # if n & (1<<k) != 0:
        #     return True
        # else:
        #     return False
        
        ##Right shift
      
        if (n>>k) & 1 != 0:
            return True
        else:
            return False
