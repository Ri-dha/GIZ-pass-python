class Solution:
    def longestPalindrome(self, s: str) -> str:
        # function to find the longest palindrome from the string

        
        def pointersfun(left,right):

            #we start from the middle of the string then go left and right to find out the longest Palindrome

            while (left >= 0 and right < len(s) and s[left]==s[right]):
                left-= 1
                right+= 1
            return s[left+1:right]

        # we store the result of the longestPalindrome
        palindrome = ""
        
        # for loop for two cases (odd number of characters string and even number of characters string)
         
        for i in range(len(s)):
            # for odd numbers characters 
            initPalndrome = pointersfun(i,i)
            if len(initPalndrome) > len(palindrome): palindrome = initPalndrome

            #two pointers for even numbers characters   
            initPalndrome = pointersfun(i,i+1)

            # check which palindrome is the longest then store it in the result variable
            if len(initPalndrome) > len(palindrome): palindrome = initPalndrome    
        print (palindrome) 

    s = input('enter a string:')
    longestPalindrome('self',s)