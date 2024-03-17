

def neg_value(array , n):
    for i in range(n):
        for j in range(i + 1, n ):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array      
    
array=[1,2,3,4,-3,-5,-8]
n=len(array)
print(neg_value(array,n))

def sort_value(array,n):
    min=0
    for i  in range(n):
        if i<min:
             min+=i
    return min 
array=[1,2,3,4,5,-0,-12]
n=len(array)
print(sort_value(array, n))

def sort_value(array, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # Swap the elements
    return array

array = [1, 2, 3, 4, 5, 0, -12]
n = len(array)
print(sort_value(array, n))

def cyclically_rotate(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

# Example usage:
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
cyclically_rotate(arr)
print("Array after cyclic rotation:", arr)


def getPairsCount(arr, n, K):
 
    count = 0  # Initialize result
 
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                count += 1
 
    return count
 
 
# Driver function
arr = [1, 5, 7, -1]
n = len(arr)
K = 6
print("Count of pairs is", getPairsCount(arr, n, K))


def reverse_array(array, n ):
    start_index=0
    last_index=n-1
    while start_index<last_index:
        array[start_index],array[last_index]=array[last_index],array[start_index]
        start_index+=1
        last_index-=1
    return array
array=[1,2,4,5,6]
n=len(array)
print(reverse_array(array,n))

def revers_array(array ,n ):
    start_index=0
    last_index=n-1
    while start_index<last_index:
        array[start_index],array[last_index]=array[last_index],array[start_index]
        start_index+=1
        last_index-=1
    return array
array=[1,2,33,5,4,22,1]
n=len(array)
print(revers_array(array,n))

def find_min_max(array):
    min=array[0]
    max=[]
    for i in array:
        if i <= min:
            min=i
            
    return min
array=[7,23,43,224,5]
print(find_min_max(array))

def find_max(array):
    max = array[0]
    for i in array:
        if i >= max:
            max=i
    return max
array=[2,3,5,6,9]
print(find_max(array))

def min_max_value(array):
    
    min_val = max_val = array[0]
    for i in array:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    return min_val , max_val
array=[25,67,44,323,432,2123,3]

min_value , max_value = min_max_value(array)
print("minimum value is :", min_value)
print("maximum value is :",max_value)

def min_max_value(array):
    min_val = max_val = array[0]  # Initialize min_val and max_val with the first element
    for i in array:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    return min_val, max_val

array = [1, 2, 3, 4, 5, 6]
min_value, max_value = min_max_value(array)
print("Minimum value is:", min_value)
print("maximum value is :", max_value)

def swap_number_in_array(arr, index1,index2):
    arr[index1],arr[index2]=arr[index2],arr[index1]
    
    
arr=[1,2,3,4,5,6,7,8]
print("original array is :", arr)

swap_number_in_array(arr , 1 , 4)
print("swap array is :" , arr) 

def swap_no_array(array , index1 , index2):
    array[index1],array[index2]=array[index2],array[index1]
my_array=[1,2,3,4,5,6,7]
print("oringnal array is :", my_array)

swap_no_array(my_array,6,5)
print("swap no in array is :",my_array)   

def linear_search(array , terget):
    for i in range(len(array)):
        if array[i] == terget:
            return i
    return -1
my_array = [1, 2, 3, 4, 5]
target_element = 4

index = linear_search(my_array,target_element)
if index != -1:
 print(f"Element {target_element} is found at index {index}.")
else:
    print(f"Element {target_element} is not found.")
    
    
def bubble_sort(array):
    n=len(array)
    for r in range(1,n):
        for i in range(n-r):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
array=[32,41,522,912,22,1222]
bubble_sort(array)
print(array)   

def selection_sort(array):
    n=len(array)
    for i in range(n):
        min_value=i 
        for j in range(i+1,n):
            if array[j]<array[min_value]:
                min_value=j
        array[i],array[min_value]=array[min_value],array[i]
array=[2,44,3,1,2,32,34,322,1]
selection_sort(array)
print(array)    

def bubble_sort(array):
    n=len(array)
    for r in range(1,n):
        for i in range(n-r):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
array=[22,332,1223,2232,1232]
bubble_sort(array)
print(array)

def selection_sort(array):
    n=len(array)
    for i in range(n):
        min_value=i
        for j in range(i+1 , n):
            if array[j]<array[min_value]:
                min_value=j
        array[i],array[min_value]=array[min_value],array[i]   
array=[1,2,32,2,32,1221,2,1,2,]
selection_sort(array)
print(array)
        
        
