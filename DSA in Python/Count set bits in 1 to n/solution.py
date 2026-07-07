class Solution:
    def countSetBits(self,n):
        # code here
     #base case
     if n==0:
        return 0;
     
     #find the x
     x = 0
     while (1<<(x+1)) <= n:
        x += 1
     
     #larget power
     p = 1<<x
     
     # Bits from 1 to (2^x - 1)
     bits1 = x*(1<<(x-1)) if x>0 else 0
     
     # MSB contribution
     msb = n - p + 1
     
     # Remaining numbers
     remaining = n - p
     
     # Recursive answer
     return bits1 + msb + self.countSetBits(remaining)
     
    
