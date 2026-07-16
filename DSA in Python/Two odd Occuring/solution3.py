class Solution:
    def twoOddNum(self, arr):
        #code here 
        #find the xor
        ans = 0
        for i in arr:
            ans ^= i
        
        #find the mask value
        mask = ans & -(ans)
        
        # setbit element in ans_set and visa vera
        # find the two odd pairs
        xor1 = 0
        xor2 = 0
        
        for i in arr:
            if i & mask:
                xor1 ^= i
            else:
                xor2 ^= i
        
        return sorted([xor1, xor2], reverse=True)
                
       
        
        
