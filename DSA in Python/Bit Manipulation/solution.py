class Solution:
    def bitManipulation(self, num, i):
        # Code here
        pos = i - 1

        get_bit = (num >> pos) & 1
        set_bit = num | (1 << pos)
        clear_bit = num & ~(1 << pos)

        print(get_bit, set_bit, clear_bit)
