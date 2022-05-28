'''Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]'''

def sort_array(source_array):
    odd=[]
    odd_pos=[]
    even_pos=[]

    for i in range(len(source_array)):
        if source_array[i]%2!=0:
            odd.append(source_array[i])
            odd_pos.append(i)
        else:
            even_pos.append(i)

       
    odd.sort()
    print(odd,even_pos,odd_pos)
    final=[]
    for i in range (len(source_array)):
        if i in even_pos:
            final.append(source_array[i])
        elif i in odd_pos:
            for z in range(len(odd_pos)):
                if odd_pos[z]==i:
                    final.append(odd[z])

    return(final)

    # Return a sorted array.

print(sort_array([5, 3, 2, 8, 1, 4]))