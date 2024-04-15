import numpy as np
import time

def knuth_sequence(N):
    k = int(np.log2(N))-1
    sequence  = [1]
    while k>1: # sequence already has one element
        sequence .append(2*sequence [-1]+1)
        k -= 1
    return sequence [::-1]


def shell(arr):
    n = len(arr)
    comparisons = 0
    moves = 0
    start_time = time.time()

    for gap in knuth_sequence(n):
        for i in range(gap, n): 
            el = arr[i]
            j = i

            comparisons += 1
            while j -gap>= 1 and arr[j - gap] > el:
                comparisons += 1
                arr[j] = arr[j - gap]
                moves += 1
                j -= gap
            
            arr[j] = el
            moves += 1

    end_time = time.time()
    func_time = end_time - start_time
    return comparisons, moves, func_time 

def generate_array(n):
    return np.random.randint(-100, 100, size=n)

a = generate_array(5)
print(a)
a_s, c, m = shell(a)
print(a, a_s, c, m)

def run_algorithm_multiple_times(algorithm, array_size, repetitions):
    total_comparisons = 0
    total_moves = 0
    total_time = 0

    for _ in range(repetitions):
        arr = generate_array(array_size)
        comparisons, moves, func_time = algorithm(arr)
        total_comparisons += comparisons
        total_moves += moves
        total_time += func_time

    avg_comparisons = total_comparisons / repetitions
    avg_moves = total_moves / repetitions
    avg_time = total_time / repetitions

    return avg_comparisons, avg_moves, avg_time

repetitions = 5

avg_c100, avg_m100, avg_t100 = run_algorithm_multiple_times(shell, 100, repetitions)
avg_c1000, avg_m1000, avg_t1000 = run_algorithm_multiple_times(shell, 1000, repetitions)
avg_c10000, avg_m10000, avg_t10000 = run_algorithm_multiple_times(shell, 10000, repetitions)

print('Average Results for Array of Size 100:')
print(avg_c100, avg_m100, avg_t100)

print('Average Results for Array of Size 1000:')
print(avg_c1000, avg_m1000, avg_t1000)

print('Average Results for Array of Size 10000:')
print(avg_c10000, avg_m10000, avg_t10000)
