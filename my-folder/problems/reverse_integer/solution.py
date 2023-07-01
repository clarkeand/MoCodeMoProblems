class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        new_num_list = []
        return_num = ""
        
        for digit in x:
            new_num_list.append(digit)

        if new_num_list[0] == '-':
            return_num += new_num_list.pop(0)

        while new_num_list != []:
            return_num += new_num_list.pop()

        return_num = int(return_num)

        if return_num >= 2147483647 or return_num <= -2147483648: 
            return 0
    
        return return_num
