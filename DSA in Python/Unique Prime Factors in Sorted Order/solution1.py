class Solution:
    def is_prime(self,n):
        if n<2:
            return 0
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return 0
        
        return 1
            
    def primeFac(self, n):
        # code here
        lis = []
        for i in range(1,n+1):
            if(n%i == 0 and self.is_prime(i)):
                lis.append(i)
        
        return lis
