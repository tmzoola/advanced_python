def binary_search(my_list, value):
    start_index = 0
    end_index = len(my_list)-1
    
    count = 0
    
    while start_index<=end_index:
        mid_point = start_index + (end_index-start_index)//2
        mid_point_value = my_list[mid_point]
        
        count=count+1
        
        if mid_point_value == value:
            return (mid_point, mid_point_value, count)
        
        elif value<mid_point_value:
            end_index = mid_point-1
        else:
            start_index = mid_point+1
        
    return None    


print(binary_search([5,7,9,19,45,56], 45))