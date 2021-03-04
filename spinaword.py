# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
#  function that takes in a string of one or more words, 
#  and returns the same string, but with all five 
#  or more letter words reversed (Just like the name of this Kata). 
#  Strings passed in will consist of only letters and spaces. 
#  Spaces will be included only when more than one word is present.





def main():
    sentence="I eat yummy APPLEs"
    lister = spin_words(sentence)


def spin_words(sentence):

    reString =" "

    #put each word into a list
    lister = list(sentence.split(" "))
    #print (lister)

    for word in lister:
        if len(word) < 5:
            x= ' '.join(map(str, lister)) 
            reString+=x
            
            
        else:
            #reverse word spelling\
            x = (word[::-1])
            reString += ' '.join(x)
             #reverse a words spelling
            
           
             
    print (reString)    
      
    #print(lister)
    
    #else reverse spelling of the word

    #unpack the list

    

if __name__ == '__main__':
    main()
    