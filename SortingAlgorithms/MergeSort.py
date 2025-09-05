'''
MergeSort
---------
Divide-and-conquer algorithm that splits array into smaller subarrays, sorts, and merges them.
https://www.notion.so/Python-IA-262e58af1807800ea99bfd36a970489e
'''

    
def merge_sort(arr): # Base case: if array has 1 or fewer elements, it's already sorteds
    if len(arr) <= 1:
        return arr
    
    # Split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursive call to sort each half
    left = merge_sort(left)
    right = merge_sort(right)
    
    
    return merge(left, right) # Combine sorted halves

def merge(left, right):
    result = []
    i = j = 0    # indices to traverse left and right arrays
    
    # Compare elements from both arrays and add smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from either array
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    arr = [92,64,34,25,54,87,23,73,291,98,12,22,11,90]
    
    sorted_arr = merge_sort(arr)
    
    print(f'''
          
    Merge Sort
    ----------
    
    Unsorted array: {arr}
       |
       |___ Sorted array: {sorted_arr}''')

if __name__ == "__main__":
        main()
    
