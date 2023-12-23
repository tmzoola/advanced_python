def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        for a in range(0,n-1):
            
            if arr[a]>arr[a+1]:
                
                arr[a], arr[a+1] = arr[a+1],arr[a]
                count=count+1
    return arr,count

arr = [1,1,2,3,6]

print(bubble_sort(arr))
