def main():
    file= open("wordCount.txt","r")

    letterCount=0
    wordCount=0
    lineCount=0
    wordList=[]

    ##Count line
    for i in file:
        lineCount+=1
        wordList.append(i.split())
        
        ##count letters
        for letter in i:
            letterCount+=1


    ##count words
    for i in wordList:
        for j in i:
            wordCount+=1
            
    print("Lines: {}\nWords: {}\nLetters: {}".format(lineCount,wordCount,letterCount))
   
       
      

if __name__=='__main__':
    main()
