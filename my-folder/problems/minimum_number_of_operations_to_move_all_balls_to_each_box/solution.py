class Solution(object):
    def minOperations(self, boxes):
        num_list = []
        result_list = []
        sum_nums = 0
        for char in boxes: 
            num_list.append(int(char))
            if char == "1":
                sum_nums += 1
            
        for i in range(len(num_list)):
            counter = 0
            for j in range(len(num_list)):
                if num_list[j] == 1:
                    counter += abs(j - i)
            result_list.append(counter)
    
        return result_list