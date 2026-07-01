class Solution:
    def reverseBits(self,n):
        #code here
        # binary = bin(n)[2:] # decimal to binary
        # rev = binary[::-1] # reverse
        # ans = int(rev,2)  # binary to decimal
        # return ans
        
        # decimal to binary
        ans = ""
        while n > 0:
            if n%2 == 1:
                ans += "1"
            else:
                ans += "0"
            n = n//2
        # binary to decimal after reversing
        res = 0
        p2 = 1
        for i in range(len(ans)-1,-1,-1):
            if ans[i] == '1':
                res += p2
            p2 *= 2
            
        return res
            
        
        
        
