class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack: 
            return -1

        possible_starts = []
        for i in range(len(haystack)):
            needle_tracker = 0
            if haystack[i] == needle[needle_tracker]:
                possible_starts.append(i)
        print(possible_starts)

        for item in possible_starts: 
            if haystack[item:(item+len(needle))] == needle:
                return item
            