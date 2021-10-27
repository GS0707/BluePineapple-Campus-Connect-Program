''' Check whether given input is palindrome or not
    (when we read from start or end of the array the word is same then it is palindrome)
    Ex. 1. 'madam' word  is palindrome.
        2. 'mabsam' word is not palindrome. 
'''
# Accept an input
isPalindrome=[i for i in input("Enter the word: ")]

i=0
j=len(isPalindrome)-1

# traverse the array
while i<j:
    # if character not match then exit(not palindrome)
    if isPalindrome[i]!=isPalindrome[j]:
        print(isPalindrome,' is not a Palindrome')
        exit(0)
    i+=1
    j-=1    
# conditions in while loop false then it's palindrome    
print(isPalindrome,' is Palindrome')        