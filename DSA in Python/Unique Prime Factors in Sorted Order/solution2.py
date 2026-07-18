class Solution:
    def primeFac(self, n):
        # code here
        lis = []
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                lis.append(i)
                while n%i == 0:
                    n = n//i
            
        if n != 1:
            lis.append(n)
        return lis
