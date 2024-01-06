import time 
import concurrent.futures
from PIL import Image, ImageFilter



img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]
start = time.perf_counter()
size=(1200,1200)

def process_image(image_name):
    img = Image.open(image_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    
    img = img.save(f"processed/{image_name}")
    
    print(f"{image_name} process done")
    

if __name__ =="__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)


finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")


# import time 
# import multiprocessing
# import concurrent.futures

# start = time.perf_counter()

# def foo(num):
#     print(f"Running {num} ....")
#     time.sleep(num)
#     return f"Done {num} ...."


# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         seconds = [5,4,3,2,1]
#         results = executor.map(foo, seconds)
        
#         for i in results:
#             print(i)

# import threading
# import time
# import concurrent.futures


# start = time.perf_counter()


# def index(secs):
#     print(f"Running in {secs} function.....")


# # with concurrent.futures.ThreadPoolExecutor() as executor:
# #     seconds = [5,4,3,2,1]
    
# #     res = [executor.submit(index, secds) for secds in seconds]
# #     for f in concurrent.futures.as_completed(res):
# #         f.result()
    

# threads = []

# for _ in range(100):
#     t = threading.Thread(target=index, args=[_])
#     t.start()
#     threads.append(t)

# for thead in threads:
#     thead.join()



# finish = time.perf_counter()

# print(f"Finished in {round(finish-start,2)} seconds")

