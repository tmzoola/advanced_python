class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i","o","u"]
        dict_a = {key:value for key, value in enumerate(s) if value in vowels}
        new_word = ""
        count = 0
        length = len(s)-1
        
        while length>0:
            if s[count] not in vowels:
                new_word+=s[count]
            elif s[count] in vowels:
                print(count, length)
               
            length-=1
            count+=1
            
        
        return new_word, dict_a
        
        

obj = Solution()
print(obj.reverseVowels("hello"))