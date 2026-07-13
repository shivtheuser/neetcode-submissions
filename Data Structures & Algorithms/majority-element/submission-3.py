class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = 0
        cnt = 0
        for i in range(0,len(nums)):
            if cnt == 0:
                current = nums[i]
                cnt += 1
            elif nums[i] == current :
                cnt += 1
            else:
                cnt -= 1
        return current
        