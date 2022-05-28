
seq=[1,2,2,3,3,3,4,3,3,3,2,2,1]
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
           
            return i

'''Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)'''
def find_it(seq):
    char_list=[]
    count_list=[]
    for char in seq:
        if char in char_list:
            pass
        else:
            char_list.append(char)
    for char in char_list:
        count=0
        for i in range(len(seq)):
            if seq[i]==char:
                print(seq[i])
                count +=1
        count_list.append(count)
    it=0
    print(count_list,char_list)
    for char in count_list:
        it+=1
        if char%2!=0:
            return(char_list[it-1])

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))