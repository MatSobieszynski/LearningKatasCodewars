'''Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!'''

import numbers


def expanded_form(num):
    numb=list(str(num))


    numbers=[]
    for i in range(len(numb)):
        print(i,len(numb))
        if int(numb[i])==0:
            pass
        else:
            z=(int(numb[i])*(10**(len(numb)-i-1)))            
            numbers.append(z)

    listToStr = ' + '.join([str(elem) for elem in numbers])


    return listToStr



print(expanded_form(9034))