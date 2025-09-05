'''
BubbleSort
----------
Simple sorting algorithm that repeatedly steps through the list, compares adjacent 
elements and swaps them if they are in the wrong order.
'''

def bubbleSort(arr):
    length = len(arr)
    for i in range(0, length - 1):
        for i in range(0, length - i - 1):
            if arr[i] > arr[i + 1]:
                flag = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = flag
    return arr
                
def main():
    arr = [92,64,34,25,54,87,23,73,291,98,12, 22, 11, 90]
    sorted_arr = bubbleSort(arr)
    
    '''The unsorted array represents the original input array and
    the sorted array shows the result after applying bubble sort'''
    
    print(f'''
    
    Bubble Sort
    ----------
    
    Unsorted array: {arr}
       |
       |___ Sorted array: {sorted_arr}''')
    
if __name__ == "__main__":
        main()
    