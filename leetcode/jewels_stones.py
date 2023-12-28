class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list_jewels = [x for x in jewels]
        total = 0

        for i in list_jewels:
            count = 0
            for j in stones:
                if i in stones:
                    count=count+1
                    stones=stones.replace(i,"",1)
            total = total + count
        return total