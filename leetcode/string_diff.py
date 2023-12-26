class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        word1 = (x for x in s)
        word2 = [x for x in t]

        for i in word1:
            word2.remove(i)
        return ''.join(word2)
obj = Solution()    
print(obj.findTheDifference("abcd", "abcde"))