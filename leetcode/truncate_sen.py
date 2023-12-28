class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list_s = s.split()
        result = []
        for i in range((len(list_s)- (len(list_s)-k))):
            result.append(list_s[i])
          
        return " ".join(result)
obj = Solution()
print(obj.truncateSentence("Hello how are you Contestant", 4))