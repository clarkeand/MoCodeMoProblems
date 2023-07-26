class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  # Return an empty string if the input list is empty

        common_chars = strs[0]  # Take the first string as the initial common prefix
        for string in strs[1:]:  # Start from the second string
            i = 0
            while i < len(common_chars) and i < len(string) and common_chars[i] == string[i]:
                i += 1
            common_chars = common_chars[:i]  # Update the common prefix

            if not common_chars:  # If common_chars becomes empty, then no common prefix exists
                break

        return common_chars
