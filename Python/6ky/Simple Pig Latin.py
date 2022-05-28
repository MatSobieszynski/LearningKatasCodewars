'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway ! '''

from os import dup


def pig_it(text):
    dupa=list(text.split(" "))
    super_dupa=[]
    count=0
    for elem in dupa:
        count+=1
        if elem in ",.!;:'":
            super_dupa.append(elem)
        if count!=len(dupa):
            print (len (dupa))
            print(count)
            print("dupa")
            z=elem[1:]
            super_dupa.append(z)
            super_dupa.append(elem[0])
            super_dupa.append("ay ")
        else:
            print("dupa2")
            z=elem[1:]
            super_dupa.append(z)
            super_dupa.append(elem[0])
            super_dupa.append("ay")

    
    return "".join(super_dupa)
    

print(pig_it('Pig latin i cool!'))