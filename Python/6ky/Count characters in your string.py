'''The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.'''

from numpy import char


def count(string):
    used_letters=[]
    count=[]
    
    for i in range(len(string)):
        if string[i] not in used_letters:
            used_letters.append(string[i])
    for letter in used_letters:
        counts=0
        for i in range(len(string)):
            if string[i]==letter:
                counts+=1
        count.append(counts)
    print(used_letters,count)
    res = {}
    res = {used_letters[i]: count[i] for i in range(len(used_letters))}      


    return res


print(count("afsajsanfas"))