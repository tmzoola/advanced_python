def buble_sort(my_list):
    len_index = len(my_list)-1
    
    sorted = False
    
    while not sorted:
        sorted = True
        
        for i in range(0, len_index):
            if my_list[i]>my_list[i+1]:
                sorted = False
                my_list[i],my_list[i+1]=my_list[i+1],my_list[i]  
    
    return my_list


print(buble_sort([10,2,4,12,8,11]))