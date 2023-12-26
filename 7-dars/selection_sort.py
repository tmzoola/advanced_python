import time
import random

list1 = []

for i in range(1,5000):
    list1.append(random.randint(1,10000))

def selection_sort(my_list):
    index_length = range(0, len(my_list)-1)
    
    for i in index_length:
        min_value = i
        
        for j in range(i+1, len(my_list)):
            if my_list[j]< my_list[min_value]:
                min_value = j
        
        if min_value !=i:
            my_list[min_value], my_list[i]= my_list[i],my_list[min_value]
            
    return my_list


time1 = time.time()
selection_sort(list1)
time2 = time.time()

print("Funksiya ishlash tezligi {} seconds ".format(time2-time1))