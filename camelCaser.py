

# Complete the solution so that the function will break up camel casing, using a space between words.
# splits camel case by using re library



import re

def main():
    s = "OnlineNowSir"
    result = solution(s)
    print(result)


def solution(s):
    str1=s
    camelBreak = re.findall(r'[a-zA-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str1)
    listToStr = ' '.join([str(elem) for elem in camelBreak])
   
    return listToStr

if __name__ == '__main__':
    main()


