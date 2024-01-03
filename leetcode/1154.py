class Solution:
    def dayOfYear(self, date: str) -> int:
        def kabisa(year):
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        return True
                    else:
                        return False
                return True
            else:
                return False
        
        days= [31,28,31,30,31,30,31,31,30,31,30,31]
        year = int(date[0]+date[1]+date[2]+date[3])
        days[1] = 29 if kabisa(year) else 28
        
        month = int(date[5]+date[6])-1
        
        res = 0
        for i in range(month-1):
            res+=days[i]
        
        res+=int(date[8]+date[9])
        
        return res