'''The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

Can you translate this drawing into an algorithm?

You will be given two dimensions
a positive integer length
a positive integer width
You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.
Examples in general form:
(depending on the language)

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
  
  You can see examples for your language in **"SAMPLE TESTS".**
Notes:
lng == wdth as a starting case would be an entirely different problem and the drawing is planned to be interpreted with lng != wdth. 
(See kata, Square into Squares. Protect trees! http://www.codewars.com/kata/54eb33e5bc1a25440d000891 for this problem).

When the initial parameters are so that lng == wdth, the solution [lng] would be the most obvious but not in the spirit of this kata so, in that case, 
return None/nil/null/Nothing or return {} with C++, Array() with Scala, [] with Perl, Raku.
In that case the returned structure of C will have its sz component equal to 0.
Return the string "nil" with Bash, PowerShell, Pascal and Fortran.'''
from turtle import width

from numpy import append


def sqInRect(lng, wdth):
    retur=[]
    if lng==wdth:
        return None

    max_poles=lng*wdth
    while max_poles>0:        
        first=min(lng,wdth)
        second=max(lng,wdth)
        print(max_poles,first)
        z=second//first
        #
        for i in range(0,z):
            print(i)
            retur.append(first)
            max_poles=max_poles-first**2
            
        lng=first
        wdth=second-first*z



    return(retur)

sqInRect(37, 14)