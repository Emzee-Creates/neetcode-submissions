class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listA = []
        listB = []
        contains = False
        for letter in s:
            listA.append(letter) 
        for letter in t:
            listB.append(letter)


        return sorted(listA) == sorted(listB)