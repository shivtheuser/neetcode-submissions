class Solution:
    def evenlyDivides(self, n):
        # code here
        cnt = 0
        newn = n
        while newn>0:
            res = newn%10
            if  res != 0 and n % res == 0:
                cnt += 1
            newn = newn//10

        return cnt
