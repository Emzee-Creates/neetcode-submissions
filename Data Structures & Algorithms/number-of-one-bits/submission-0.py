class Solution:
    def hammingWeight(self, n: int) -> int:
        string_n = bin(n)
        counter = 0
        for letter in string_n:
            if letter == "1":
                counter += 1

        return counter 