'''#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!'''
from operator import length_hint


def find_missing_letter(chars):
    order=[]
    for char in chars:
        order.append(ord(char))
    new_order=[]
    for i in range(1,len(order)):
        if order[i-1]==order[i]-1:
            new_order.append(order[i-1])
        else:
            new_order.append(order[i-1])
            new_order.append(order[i-1]+1)
            z=(order[i-1]+1)
            new_order.append(order[i])
            
    return(chr(z))

        

    return new_order



print(find_missing_letter(['a','b','c','d','f']))