import threading
import time
import concurrent.futures


start = time.perf_counter()


def index(secs):
    print(f"Running in {secs} function.....")


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     seconds = [5,4,3,2,1]
    
#     res = [executor.submit(index, secds) for secds in seconds]
#     for f in concurrent.futures.as_completed(res):
#         f.result()
    

threads = []

for _ in range(100):
    t = threading.Thread(target=index, args=[_])
    t.start()
    threads.append(t)

for thead in threads:
    thead.join()



finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")