'''Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']'''
def solution(s):
    zupa=[]
    count=0
    for elem in range(len(s)):
        count+=1

        if count%2==0:
            z=str(s[elem-1])
            a=str(s[elem])
            zupa.append(z+a)
            print(zupa)
        elif count==len(s):
            z=str(s[elem])
            zupa.append(z+"_")
    return(zupa)
        
print(solution('asdfadsf'))