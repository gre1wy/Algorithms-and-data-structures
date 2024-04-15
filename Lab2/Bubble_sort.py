import numpy as np
import time


def bubbleSort(array):
    comparisons = 0
    moves = 0
    start_time = time.time()
    # прохід по масиву
    for i in range(len(array)):
        
        # перевірка на присутність зміни місць елементів
        swapped = False
    
        # прохід по масиву (від усіх елементів до одного)
        for j in range(0, len(array) - i - 1):
            comparisons += 1
            # порівняння двух елементів
            if array[j] > array[j + 1]:
                # обмін елементів якщо вони не впорядковані
                array[j], array[j+1] = array[j+1], array[j]
                moves += 1
                swapped = True
            
        # якшо після і-того прохода ніякі елементи не змінили місця зупиняємось
        if not swapped:
            break
    end_time = time.time()
    func_time = end_time - start_time
    return comparisons, moves, func_time

def generate_array(n):
    return np.random.randint(-100, 100, size=n)

array_100 = generate_array(100)
array_1000 = generate_array(1000)
array_10000 = generate_array(10000)

c100, m100, t100 = bubbleSort(array_100)
c1000, m1000, t1000 = bubbleSort(array_1000)
c10000, m10000, t10000 = bubbleSort(array_10000)
print('Sorted Array 100 in Ascending Order:')
print(c100, m100, t100)
print('Sorted Array 1000 in Ascending Order:')
print(c1000, m1000, t1000)
print('Sorted Array 10000 in Ascending Order:')
print(c10000, m10000, t10000)