def rot13(message):
    newS = "" 
    new=""  
    
    for i in range(len(message)):      
        val = ord(message[i].lower())
        print(val)
        shift=13  
        if message[i].isalpha()==False:
            newS+=message[i]

        elif val + 13>122:
            shift -= (122-val)
            shift = shift % 26
            newS += chr(96 + shift)             
        else:
            newS += chr(val + shift)  
    for i in range(len(message)):
        if message[i].isupper()==True:
            new+=newS[i].upper()
        else:
            new+=newS[i]
           
    
    return(new)

print(rot13("Test dupy"))