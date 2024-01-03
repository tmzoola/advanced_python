class Solution:
    def uniqueMorseRepresentations(self, words: str) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        result = []
        
        for word in words:
            string_all = ""
            for j in word:
                string_all +=code[alphabet.index(j)]
            
            result.append(string_all)
        return len(set(result))

obj = Solution()
print(obj.uniqueMorseRepresentations(["gin","zen","gig","msg"]))