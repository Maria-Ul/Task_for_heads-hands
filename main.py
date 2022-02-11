import numpy as np
import random
def func(n):
    sizes = []
    while len(sizes)!=n:
        s = random.randint(1,n*2)
        if s in sizes:
            s = random.randint(1, n * 2)
        else: sizes.append(s)
    list_of_arrays = []
    for i in range(n):
        list_of_arrays.append([random.random()*n*2 for i in range(sizes[i])])
#sort max
    for i in range(0,n,2):
        list_of_arrays[i].sort()
#sort min
    for i in range(1,n,2):
        list_of_arrays[i].sort(reverse = True)
    return list_of_arrays

if __name__ == '__main__':
    func(5)
