'''Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice  '''

from configparser import DuplicateOptionError
from curses.ascii import isalpha
from itertools import count


def duplicate_count(text):
    zabawa=[]
    for elem in text:
        if elem.isalpha()==True:            
            elem=elem.upper()
            zabawa.append(elem.lower())
        else:
            zabawa.append(elem)
    hej="".join(zabawa)
         
 
    char_list=[]
    count_list=[]
    for elem in hej:
        if elem not in char_list:
            char_list.append(elem)
    for char in char_list:
        count=0
        for i in range(len(hej)):
            if char==hej[i]:
                count+=1
        count_list.append(count)

    counts=0
    for elem in count_list:
        if elem >1:
            counts+=1
    return counts

print(duplicate_count("Indivisibilities"))
    
     