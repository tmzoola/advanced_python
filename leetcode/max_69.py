class Solution:
    def maximum69Number (self, num: int) -> int:
        new_num = [x for x in str(num)]
        if "6" in new_num:
            index_of = new_num.index("6")
            new_num[index_of] = "9"
            return int("".join(new_num))
        else:
            return num

obj1 = Solution()
print(obj1.maximum69Number(9999))