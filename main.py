#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word1):
    word1=word1.replace(" ","")
    if word1.isspace():
        return(False)
    word1 = word1.lower()
    x=-1
    for i in word1:
        if i == word1[x]:
            x-=1
        else:
            return(False)
    return(True)



if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word=input()
    print(palindrome(word))

