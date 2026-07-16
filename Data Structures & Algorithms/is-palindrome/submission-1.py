class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        r = []
        t = []
        for letter in s:
            if letter.isalnum():
                r.append(letter)

        t = r[::-1]
        return t == r