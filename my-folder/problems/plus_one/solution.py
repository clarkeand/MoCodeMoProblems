class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # set parameter to end at length of list
        x = len(digits) - 1
        while x >= 0: 
            # if this is the first iteration add 1 to the number
            if x == len(digits) - 1: 
                digits[x] = digits[x] + 1
            # now as we iterate the list check if a value == 10 and either: 
            if digits[x] == 10: 
                digits[x] = 0
                # add 1 to the 'next'/previous index
                if x > 0:
                    digits[x-1] += 1
                # create new index if 'previous' index doesn't exist.
                else:
                    digits.insert(0,1)
            
            x -= 1

        #return our now adjusted list
        return digits