'''Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: r must be without duplicates.
'''
def in_array(array1, array2):
    print(array1)
    dupa=[]
    for elem in array1:
        for i in range(len(array2)):
            if elem in array2[i] and elem not in dupa:
                dupa.append(elem)

    # your code
    return sorted(dupa)


print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
        