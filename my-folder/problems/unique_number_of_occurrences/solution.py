class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = dict()
        
        for num in arr:
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num]+=1
                
        unique_list = []
        
        for key in counter.keys():
            if counter[key] in unique_list: 
                return False
            else:
                unique_list.append(counter[key])
        return True