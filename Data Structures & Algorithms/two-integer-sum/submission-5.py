class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            
            res = target - nums[i]
            if res in mp and mp[res] != i:
                return [mp[res],i]
            mp[nums[i]] = i
        return []
        