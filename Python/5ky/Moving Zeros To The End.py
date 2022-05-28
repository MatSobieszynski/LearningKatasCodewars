def move_zeros(array):
    zeros=[]
    full=[]
    for elem in array:
        if elem ==0:
            zeros.append(elem)
        else:
            full.append(elem)
    for elem in zeros:
        full.apend(elem)
            
    return full



print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))