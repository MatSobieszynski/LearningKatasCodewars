'''Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).'''

def two_sum(numbers, target):
    z=[]
    for i in range(0,len(numbers)):
        
        
        for j in range(0,len(numbers)):
            if j!=i:
                zqz=numbers[i]+numbers[j]

                if zqz == target and len(z)!=2:
                    z.append(i)
                    z.append(j)
                    break
    return (z)

print(two_sum([2,2,3], 4))
