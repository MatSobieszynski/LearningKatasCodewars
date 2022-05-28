'''Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"'''
def spin_words(sentence):
    li = list(sentence.split(" "))
    end=[]
    count=0
    for char in li:        
        if len(char)<5 :
            end.append(char)
        else:
            end.append(char[::-1])
        count+=1
    
    # Your code goes here
    return " ".join(end)



print(spin_words( "Hey fellow warriors" ))