'''You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm).

Note
consecutive strings : follow one after another without an interruption'''

def longest_consec(strarr, k):
    print(strarr,k)
    if len(strarr)==0 or k <=0 or k>len(strarr):
        return ""
    zups=[]
    lenght=[]
    if k!=1:
        for i in range(len(strarr)-k+1):
            new=""
            for ks in range(k):
                new=new+(strarr[i+ks])
            zups.append(new)
    elif k==1:
        for i in range(len(strarr)):
            zups.append(strarr[i])        
    for elem in zups:
        lenght.append(len(elem))
    max_l=0

    for elem in lenght:
        if elem>max_l:
            max_l=elem

    for i in range(len(lenght)):
        if max_l==lenght[i]:
            return zups[i]


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))