class Solution:
    def removeElement(self, nums: int, val: int) -> int:
        while nums.count(val)>0:
            nums.remove(val)
        return len(nums)
    
obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2],2))