class Solution:
    def shuffle(self, nums: int, n: int) -> int:
        i = 0
        result = []
        
        while i<n:
            result.append(nums[i])
            result.append(nums[i+n])
            i = i+1
        return result
    
    
obj1 = Solution()
print(obj1.shuffle([2,5,1,3,4,7],3))