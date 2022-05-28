'''This time no story, no theory. The examples below show you how to write function accum:
import string
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Ttt'''
import string
def accum(s):
    new_list=list(s)
    sum_list=[]
    for i in range(len(new_list)):
        if i==0:
            z=new_list[i]
            sum_list.append(z.upper())
            sum_list.append("-")
            print(sum_list)           
        else:
            for d in range(i+1):
                z=new_list[i]                
                if d==0:                    
                    sum_list.append(z.upper())
                else:
                    sum_list.append(z.lower())
            sum_list.append("-")
    sum_list.pop()
    return "".join(sum_list)
  
                    
                       



print(accum("abcd"))