class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""

        for ch in s:
            if ch.isalnum():
                a += ch.lower()

        i = 0
        j = len(a)-1

        while i<j:
            if a[i] != a[j]:
                return False
            i+=1
            j-=1
        return True