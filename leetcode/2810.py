class Solution:
    def finalString(self, s: str) -> str:
        list_a = []
        
        for i in s:
            if i == "i":
                list_a = list_a[::-1]
            else:
                list_a.append(i)
        return "".join(list_a)
    
obj = Solution()
print(obj.finalString("string"))