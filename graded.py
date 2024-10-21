import numpy as np
import torch

from itertools import permutations

def signed_sort(abc):
    indexed_abc = list(enumerate(abc))
    indexed_abc.sort(key=lambda x: x[1])
    
    num_swaps = 0
    visited = [False] * len(abc)
    
    for i in range(len(abc)):
        if visited[i] or indexed_abc[i][0] == i:
            continue
        
        cycle_length = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = indexed_abc[j][0]
            cycle_length += 1
        
        if cycle_length > 0:
            num_swaps += (cycle_length - 1)
    
    sign = -1 if num_swaps % 2 else 1
    
    sorted_abc = [x[1] for x in indexed_abc]
    
    return sorted_abc, sign

def anti_symmetrize(abc):
    abc = permutations(abc)
    abc = list(abc)
    abc = [''.join(p) for p in abc]
    sign = [signed_sort(abc[i])[1] for i in range(len(abc))]
    return abc, sign

def cyclic(abc):
    n = len(abc)
    if isinstance(abc, str):
        return ''.join([abc[(i+1) % n] for i in range(n)])
    return [abc[(i+1) % n] for i in range(n)]

def anti_symmetrize_array(array):
    n_index = len(array.shape)

    index = [chr(ord('a') + i) for i in range(n_index)]
    index = ''.join(index)

    indices, signs = anti_symmetrize(index)

    array = [signs[i] * np.einsum(index, array) 
             for i, index in enumerate(indices)]
    array = sum(array)

    return array

def anti_symmetrize_tensor(tensor):
    n_index = len(tensor.shape)

    index = [chr(ord('a') + i) for i in range(n_index)]
    index = ''.join(index)

    indices, signs = anti_symmetrize(index)

    try:
        tensor = [signs[i] * torch.einsum(index, tensor) 
                 for i, index in enumerate(indices)]
   
        tensor = sum(tensor)

    except:
        print('Not antismmetrizable')

    return tensor


