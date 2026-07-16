class Solution:
    def twoOddNum(self, arr):
        #code here 
        mp = {}
        for val in arr:
            mp[val] = mp.get(val,0)+1
        lis = []
        for key,val in mp.items():
            if mp[key] & 1:
                lis.append(key)
        lis.sort(reverse = True)
        return lis
        
    
