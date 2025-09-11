''' 
- The binary search, algorithm is  an efficient method for finding a specific value within a sorted list.
It works by repeatedly dividing the search interval in half until the desired value is found or the interval is empty.
but the list must be sorted before performing a binary search. 

'''

N = [41, 3, 6, 5, 9, 36, 23, 12, 19, 29, 15, 27, 30, 11, 8]

def BinarySearch(lista, target) -> int:
    lista = sorted(lista)
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == target:
            return medio
        
        if lista[medio] < target:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1

BinarySearch(N, 19)