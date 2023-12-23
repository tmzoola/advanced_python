nums = [1,2,3] #iterable
iterator_nums = iter(nums) #iterator
 
while True:
    try:
        item = next(iterator_nums)
        print(item)
    except StopIteration:
        break


class MyRange:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >=self.end:
            raise StopIteration
        
        self.start+=1
        return self.start -1 

nums = MyRange(1,10)

for i in nums:
    print(i)









