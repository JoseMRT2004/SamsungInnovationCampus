'''
- The linear search algorithm is a straightforward method for finding a specific value within a list.
It works by checking each element in the list sequentially until the desired value is found or the end of the list is reached.

'''

N = [41, 3, 6, 5, 9, 36, 23, 12, 19, 29, 15, 27, 30, 11, 8]

def LinearSearch(lista, target) -> int:
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

LinearSearch(N, 19)