class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s[::-1]
        elif len(s)<2*k:
            return s[:k][::-1] + s[k:]
        else:
            list_a = [s[i:i+2*k] for i in range(0, len(s), 2*k)]
            res = []
            for i in list_a:
                if len(i)>k:
                    res.append(i[:k][::-1] + i[k:])
                else:
                    res.append(i[::-1])
            return "".join(res)
            
            
            

obj = Solution()
print(obj.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",39))

expected = "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"
result =   "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"