class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for i in range(0,len(nums)):
            if nums[i] in l:
                return True
            else:
                l.append(nums[i])
        return False
