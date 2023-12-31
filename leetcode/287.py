class Solution:
    def findDuplicate(self, nums: int) -> int:
        start = 0
        ss = 0
        finish = 0
        while start == 0 or nums[start] != nums[finish]:
            start = nums[start]
            finish = nums[nums[finish]]
        while nums[ss] != nums[start]:
            ss = nums[ss]
            start = nums[start]
        return nums[ss]