# -*- coding: cp1251 -*-

i = 0
n = int(input('Enter a number of disks: '))
towers = {'A': [], 'B': [], 'C': []}

def print_tower_state(towers):
    for tower, disks in towers.items():
        print(f"{tower}: {disks}")
        

for disk in range(n, 0, -1):
        towers['A'].append(disk)
        

print("Початковий стан веж:")
print_tower_state(towers)



def hanoi_towers(n, start, middle, end, towers):
    if n > 0:
        # Move n-1 disks from start to middle tower
        hanoi_towers(n - 1, start, end, middle, towers)

        # Move the nth disk from start to end tower
        global i
        i += 1
        print(f"{i}-a дія: Перемістити диск {n} з {start} в {end}")
        towers[end].append(towers[start].pop())  # Move disk from start to end
        print_tower_state(towers)

        # Move the n-1 disks from middle to target tower
        hanoi_towers(n - 1, middle, start, end, towers)
        

hanoi_towers(n, 'A', 'B', 'C', towers)
