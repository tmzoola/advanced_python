class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i","o","u","A", "E", "I","O","U"]
        vowels_list = [i for i in s if i in vowels]
        
        print(vowels_list)

        result = ""
        
        for letter in s:
            if letter in vowels:
                result = result + vowels_list.pop()
            else:
                result+=letter
        
        return result
        
    
obj = Solution()
print(obj.reverseVowels("hello"))