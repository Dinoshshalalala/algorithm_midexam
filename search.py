import random
import time
import matplotlib.pyplot as plt

# Linear Search
def linearSearch(array, n, x):
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
      
# Binary Search
def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
        
#fibonacci search    
def fibonacciSearch(array, x):
    size = len(array) 
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
   
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if array[index] < x:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > x:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (array[size - 1] == x):
        return size - 1
    return -1
#----------------------------------------------------
#list S with random 10 integers
def create_list(size):
    list1 = []
    for i in range(size):
        list1.append(random.randint(1, 100000000))
    return list1

# 隨機整數x
def create_x():
    x = random.randint(1, 100000000)
    return x

#-------------------main-----------------------------
def main(size):
    linear_time = []
    binary_time = []
    fibonacci_time = []
    
    for i in range(5):
        list1 = create_list(size)
        x = create_x() 
        
    # run linear search
        start1 = time.perf_counter()
        result1 = linearSearch(list1, len(list1), x)
        end1 = time.perf_counter()
        linear_time.append(end1-start1)
        print("<<run linear Search>>")
        #第幾次
        print("第", i+1 ,"次")
        if(result1 == -1):
            print("Element not found")
        else:
            print("Element found at index: ", result1)
            
    # run binary search           
        start2 = time.perf_counter()
        result2 = binarySearch(list1, x, 0, len(list1)-1)
        end2 = time.perf_counter()
        binary_time.append(end2-start2)
        print("<<run Binary Search>>")
        #第幾次
        print("第", i+1 ,"次")
        if(result2 == -1):
            print("Element not found")
        else:
            print("Element found at index: ", result2)
            
    # run fibonacci search           
        start3 = time.perf_counter()
        result3 = fibonacciSearch(list1, x)
        end3 = time.perf_counter()
        fibonacci_time.append(end3-start3)
        print("<<run Fibonacci Search>>")
        #第幾次
        print("第", i+1 ,"次")
        if(result3 == -1):
            print("Element not found")
        else:
            print("Element found at index: ", result3)
        print("--------------------------------")
    
    print("")    
    print("<----------mean time----------->")    
    mean_time1 = sum(linear_time)/5
    
    print("linear Search mean time:", mean_time1)
    print("")
#----------------------------------------------------
    mean_time2 = sum(binary_time)/5
    
    print("Binary Search mean time:", mean_time2)
    print("")
#----------------------------------------------------
    mean_time3 = sum(fibonacci_time)/5
    
    print("Fabonacci Search mean time:", mean_time3)
        
#----------------------------------------------------
# 從 n=10 ~ n=1000，執行100次
for i in range(100):
    print("")
    n = 10+10*i
    print("n=", n)
    main(n)


   