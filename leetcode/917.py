class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        list_a = [i for i in s if i.isalpha()][::-1]
        for index, value in enumerate(s):
            if not value.isalpha():
                list_a.insert(index, value)
            
        return "".join(list_a)
    
    
obj = Solution()
print(obj.reverseOnlyLetters("a-bC-dEf-ghIj"))