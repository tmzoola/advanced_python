def insertion_sort(my_list):
    indexing_length = range(1,len(my_list))
    
    for i in indexing_length:
        value_to_sort = my_list[i]
        
        while my_list[i-1]>value_to_sort and i>0:
            my_list[i],my_list[i-1]=my_list[i-1], my_list[i]
            i-=1
    
    return my_list
            



print(insertion_sort([8,5,9,12,7,1,2]))
        
    