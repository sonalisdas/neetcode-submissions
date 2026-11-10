class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i in range (0,len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                p=target-nums[i]
                break
        for k in range(i+1,len(nums)):
            if p==nums[k]:
                return [i,k]
        
    
        