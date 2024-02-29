#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word1):
    if word1 == "":
        return(False)
    elif (word1.isspace()) == False:
        word1.replace(" ","")
    word1 = word1.lower
    word2 = word1[::-1]
    if word2==word1:
        return(True)
    else:
        return(False)



if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word=input()
    print(palindrome(word))

