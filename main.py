import random

number= random.randint(50,100)

list_nums = list(range(50,101))

def binary_search(list_a, value):
    start_index = 0
    end_index = len(list_a)-1
    count = 0
    while start_index<=end_index:
        mid_point = (start_index+ end_index)//2
        mid_value = list_a[mid_point]
        
        
        if mid_value==value:
            return (mid_point, mid_value)
        
        elif mid_value<value:
            print("Guess higher")
            start_index = mid_point
        else:
            print("Guess lower")
            end_index = mid_point
    return None

print(binary_search(list_nums, number))