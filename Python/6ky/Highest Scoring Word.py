'''Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.'''

def high(x):
    li = list(x.split(" "))
    scores=[]
    for word in li:     
        score=0
        for letter in word:
            score=score+ord(letter)-96
        scores.append(score)
    max=0
    numer=0
    for i in range(len(scores)):
        if scores[i]>max:
            max=scores[i]
            numer=i
    return(li[numer])


  
  
print(high('what time are we climbing up the volcano aa'))