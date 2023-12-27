class Solution:
    def missingNumber(self, nums) -> int:
        list_len = len(nums)
        max_num = max(nums)
        if 0 not in nums:
            return 0
        elif list_len-1 == max_num:
            return list_len
        else: 
            numbers = range(min(nums), max(nums)+1)
            new_num = next(x for x in numbers if x not in nums)
            return new_num
        
        
obj1 = Solution()
print(obj1.missingNumber([1,0,3]))