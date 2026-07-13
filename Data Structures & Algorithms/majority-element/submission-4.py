class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        maxi = 0
        for i in nums:
            mp[i] = mp.get(i,0)+1
            maxi = max(maxi,mp[i])
        
        for key,value in mp.items():
            if maxi == value:
                return key