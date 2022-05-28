'''The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
 Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!'''

def duplicate_encode(word):
    zabawa=[]
    for elem in word:
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
    new_list=[]
    for i in range(len(char_list)):
            if count_list[i]>1:
                new_list.append(")")
            else :
                new_list.append('(')
    print(count_list,char_list,hej)
    baza=[]
    for elem in hej:
        for i in range(len(char_list)):
            if char_list[i]==elem:
                baza.append(new_list[i])

    return "".join(baza)

print(duplicate_encode("Success"))