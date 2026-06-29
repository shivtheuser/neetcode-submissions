class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        maxi = 0
        for i in nums:
            mp[i] = mp.get(i,0)+1
            if mp[i]>len(nums)//2:
                return i
       
        
        