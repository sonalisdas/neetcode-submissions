class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in range(0,len(s)):
            if s[i].isalnum():
                a+=s[i].lower()
        i=0
        j=len(a)-1
        while (i<len(a)/2):
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True
        

        