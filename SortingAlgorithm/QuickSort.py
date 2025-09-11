'''
Quicksort
---------
Divide-and-conquer algorithm that selects a pivot element and partitions the array around it.
The array is recursively sorted by applying the same process to the sub-arrays.
'''

def Quicksort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (in this case, the last element)
    pivot = arr[-1]
    
    # Initialize arrays for elements less than, equal to, and greater than pivot
    left = []
    middle = []
    right = []
    
    
    for x in arr: # Partition the array around the pivot
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    # Recursively sort left and right sub-arrays and combine the results
    return Quicksort(left) + middle + Quicksort(right)

def main():
    arr = [92,64,34,25,54,87,23,73,291,98,12, 22, 11, 90]
    
    sorted_arr = Quicksort(arr)
    
    print(f''' 
          
    Quick Sort
    ----------
    
    Unsorted array: {arr}
       |
       |___ Sorted array: {sorted_arr}''')
    
if __name__ == "__main__":
    main()
    