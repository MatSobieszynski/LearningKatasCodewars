'''Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer'''
def square_digits(num):
    zab=list(str(num))
    new=[]
    for elem in zab:
        new.append(int(elem)*int(elem))
    values = ''.join([str(i) for i in new])
    return(int(values))

print(square_digits(9119))