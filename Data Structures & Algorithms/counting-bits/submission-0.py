class Solution:
    def countBits(self, n: int) -> List[int]:
        my_list = []
        for i in range(n+1):
            binary = bin(i).count("1")
            my_list.append(binary)

        return my_list
