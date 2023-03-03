#NAMA   : Muhammad Nabil
#NIM    : 2209116046

import random
import os
os.system('cls')

list = []
for i in range(9):
    list.append(random.randint(1,100))

def QuickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list [0] 
        left = [x for x in list[1:] if x <= pivot]
        right= [x for x in list[1:] if x >= pivot]
        return QuickSort(left) + [pivot] + QuickSort(right)

print(f'\nList sebelum di urutkan : {list}\n')
print(f'List setelah di urutkan : {QuickSort(list)}\n\n')