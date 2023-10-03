class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result_array = []
        greatest = 0 

        for item in candies:
            if item > greatest: 
                greatest = item
        
        for item in candies: 
            if item + extraCandies >= greatest:
                result_array.append(True)
            else:
                result_array.append(False)
        return result_array