class Solution:

    def getDivisors(self, n):
        # code here
        lis = []
        lis1 = []
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                lis.append(i)
                if i != n//i:
                    lis1.append(n//i)
        return lis + lis1[::-1]
