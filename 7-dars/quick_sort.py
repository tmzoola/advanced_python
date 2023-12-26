import time
import random

list1 = []

for i in range(1,5000):
    list1.append(random.randint(1,10000))

def quick_sort(my_list):
    length=len(my_list)
    
    if len(my_list)<=1:
        return my_list
    else:
        pivot = my_list.pop()
    
    items_katta = []
    items_kichik = []
    
    for i in my_list:
        if i>pivot:
            items_katta.append(i)
        else:
            items_kichik.append(i)
            
    return quick_sort(items_kichik) + [pivot] + quick_sort(items_katta)

time1 = time.time()
quick_sort(list1)
time2 = time.time()

print("Funksiya ishlash tezligi {} seconds ".format(time2-time1))