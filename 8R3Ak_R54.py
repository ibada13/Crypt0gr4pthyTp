import threading
import math
import os
import time

MAX_THREADS = 3
total_nums = 0 
tested_nums = 0 
lock = threading.Lock()
factors = []
def progress():
    progress = 0
    while int(progress +  1 )!= 100:
        with lock:
            progress = (tested_nums / total_nums) * 100

        os.system("cls")  
        # print(int(progress+1))
        print(f"Progress: {progress:.2f}%")
        
        # if tested_nums+1 == total_nums:
            # break 
        time.sleep(1)  

def find_factors_in_range(n: int, start: int, end: int, thread_id: int):
    global tested_nums  
    for i in range(start, end):
        with lock:
            tested_nums += 1 
        if n % i == 0:
            factors.append(i)

def main(n: int):
    global total_nums
    global tested_nums
    total_nums = math.isqrt(n) + 1 
    
    progress_thread = threading.Thread(target=progress)
    progress_thread.start()

    sqrt_n = math.isqrt(n)
    range_per_thread = max(1, sqrt_n // MAX_THREADS)

    threads = []

    for thread_id in range(MAX_THREADS):
        start = thread_id * range_per_thread + 1
        end = min((thread_id + 1) * range_per_thread + 1, sqrt_n + 1)
        thread = threading.Thread(target=find_factors_in_range, args=(n, start, end, thread_id))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    progress_thread.join()

if __name__ == "__main__":
    s = "   "  
    n = int(s)
    ft = time.time()
    main(n)
    print("time to fisnih exuting : " , time.time() - ft )
    print("factors are : " ,factors)
