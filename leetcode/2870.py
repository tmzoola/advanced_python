class Solution:
    def minOperations(self, nums: int) -> int:
        new_num = list(set(nums))
        return new_num



obj = Solution()
print(obj.minOperations([2,3,3,2,2,4,2,3,4]))