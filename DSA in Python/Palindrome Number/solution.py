class Solution:
    def isPalindrome(self, n):
		# code here
		n = abs(n)
		    
		original = n
		new_n = 0
		p = 1
		while n>0:
		    rem = n%10
		    new_n = new_n*10 + rem
		    n = n//10
	    return original == new_n
