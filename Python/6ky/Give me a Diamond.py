'''You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. 
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"'''

def diamond(n):
    if n<1 or n%2==0:
        return None
    else:
        
        new=""
        for i in range(1,n+1):
            if i<int((n-1)/2+1):                
                new=new+" "*int((n-2*i+1)/2)+(2*i-1)*"*"+"\n"
            elif i==int((n-1)/2)+1:
                new=new+(2*i-1)*"*"+"\n"
            elif i>int((n-1)/2)+1:
                print(i,n)
                new=new+" "*int((n-1)/2-n+i)+(2*(n-i)+1)*"*"+"\n"

    # Make some diamonds!
    return (new)
print(diamond(7))