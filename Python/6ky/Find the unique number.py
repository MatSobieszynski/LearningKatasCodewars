'''There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique'''

def find_uniq(arr):
    for elem in arr:
        if arr.count(elem)==1:
            return elem
        

def find_unique (arr):
    unique=[]
    count=[]
    for elem in arr:
        if elem not in unique:
            unique.append(elem)
    for elem in unique:
        countt=0
        for z in range(len(arr)):
            if arr[z]==elem:
                countt+=1
        count.append(countt)
    for elem in range(len(count)):
        if count[elem]==1:
            return unique[elem]

print(find_unique([ 0, 0, 0.55, 0, 0 ]))