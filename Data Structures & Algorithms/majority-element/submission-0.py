class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        maxi = 0
        for i in nums:
            mp[i] = mp.get(i,0)+1
            maxi = max(maxi,mp[i])
        for key,freq in mp.items():
            if freq == maxi:
                return key
        
        