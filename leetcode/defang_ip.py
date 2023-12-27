class Solution:
    def defangIPaddr(self, address: str) -> str:
        add_1 = [x for x in address]
        
        while "." in add_1:
            index = add_1.index(".")
            add_1[index]="[.]"
        return "".join(add_1)
            
        

obj = Solution()
print(obj.defangIPaddr("1.1.1.1"))