def power(x, n):
    # Базовий випадок: x^0 = 1
    if n == 0:
        return 1
    # Рекурсивний випадок: x^n = x * x^(n-1)
    else:
        return x * power(x, n-1)
"""
power(x, n) = x * power(x, n-1) -> power(x, n-1) = x * power(x, n-2) -> power(x, n-2) = x * power(x, n-3) -> ... -> power(x, n-n) = 0 
"""

i=0

def hanoi_towers(n, start, middle, end): # n - number of disks; start, middle, end - three towers
    if n>0:
        # Move n-1 disks from start to middle tower
        hanoi_towers(n - 1, start, end, middle)
    
        # Move the nth disk from start to end tower
        global i
        i += 1
        print(f"{i} Перемістити диск {n} з {start} в {end}")

        # Move the n-1 disks from middle to target tower
        hanoi_towers(n - 1, middle, start, end)


def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
   
    
print ("Сума перших пяти натуральних чисел:")
print(sum_of_natural_numbers(5))



