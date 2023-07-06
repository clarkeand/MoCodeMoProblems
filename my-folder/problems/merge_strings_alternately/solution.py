class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_string = ""
        word1=list(word1)
        word2=list(word2)

        while word1 != [] or word2 !=[]:
            if word1 != []:
                new_string += word1.pop(0)
            if word2 != []:
                new_string += word2.pop(0)

        return new_string