import math
class Solution:
    def constructRectangle(self, area: int) -> int:
        result = []
        for i in range(1,area+1):
            if area%i==0:
                result.append([i,area//i]) 
                
        return result[len(result)//2]
                
obj = Solution()
print(obj.constructRectangle(6))