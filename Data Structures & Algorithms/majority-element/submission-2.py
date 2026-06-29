class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = 0
        count = 0
        for i in range(0,len(nums)):
            if count == 0:
                cand = nums[i]
                count += 1
            elif cand != nums[i]:
                count -= 1
            else:
                count += 1
        return cand

        