"""
https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

Program slices strings to eliminate the web address headings
leaving just the domain name
"""

from urllib.parse import urlparse

def main():

    #scheme from url lib is seen with HTTP or HTTPS Automatically
    # you need to write the if in url function understanding that
    
    url="www.io.io/sdfa"#TEST1

 
    reducedURL = domain_name(url) 
    print (reducedURL)
   

def domain_name(url):
    t = ((urlparse(url).netloc))
    #if header http or https header is presented
    if len(urlparse(url).scheme) >= 1:
        if 'www.' in url:
           
            reducedURL = ('.'.join(t.split('.')[1:2]))            
        else:
            print('you are in nested if block') 
            reducedURL = ('.'.join(t.split('.')[0:1]))      
    t = ((urlparse(url).path))
    #if no http or https header
    if 'www.' in url:     
        reducedURL = ('.'.join(t.split('.')[1:2]))
    else:
        print('here')
        reducedURL = ('.'.join(t.split('.')[0:1]))

    return reducedURL
   

if __name__ == '__main__':
    main()
    