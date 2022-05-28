'''The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false'''  
def generate_hashtag(s):
    if s=="":
        return False
    new="#"
    for i in range(len(s)):
        if i == 0 and s[i]!=" ":
            new=new+s[i].upper()
        elif s[i]==" ":
            pass
        elif s[i-1]==" ":
            new=new+s[i].upper()
        else:
            new=new+s[i].lower()

    if len(new)>140:
        return False
    else:
        return new
    print(new)



print(generate_hashtag(' iqGZSWtDjU mSDNmtbYfUk at kQcCMkNK'))
