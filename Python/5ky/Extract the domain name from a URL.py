'''Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"'''


def domain_name(url):
    dots_counter=0
    for elem in url:
        if elem==".":
            dots_counter+=1
    dots_position=[]
    slash_pos=[]        
    for i in range(len(url)):
        if url[i]==".":
            dots_position.append(i)
        elif url[i]=="/":
            slash_pos.append(i)
    if "www" not in url and "http" not in url:
        return (url[:dots_position[0]])
    if "www"in url:
        return(url[dots_position[0]+1:dots_position[1]:])
    else:
        return(url[slash_pos[1]+1:dots_position[0]])



print(domain_name("https://youtube.com"))