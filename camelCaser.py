

# Complete the solution so that the function will break up camel casing, using a space between words.
# Example

#how to split camel case
#join library

import re

def main():
    s = "connectedOnlineNow"
    result = solution(s)
    #print (result)


def solution(s):
    str1=s

    #re needs work
    camelBreak = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str1)
    listToStr = ' '.join([str(elem) for elem in camelBreak])
    print (listToStr)
    return listToStr

if __name__ == '__main__':
    main()


