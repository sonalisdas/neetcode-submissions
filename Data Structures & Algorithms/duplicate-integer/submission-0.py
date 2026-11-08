class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        p=[]
        for i in range(len(nums)):
            if nums[i] in p:
                return True
            else:
                p.append(nums[i])
        return False