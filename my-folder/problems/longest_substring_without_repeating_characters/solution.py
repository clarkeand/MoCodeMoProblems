class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # Initialize the variables
        start = 0  # Start index of the current substring
        max_length = 0  # Length of the longest substring found so far
        char_index_map = {}  # Dictionary to store the index of each character in the substring

        for i, char in enumerate(s):
            # If the character is already in the substring, update the start index accordingly
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1

            # Update the character's index in the dictionary
            char_index_map[char] = i

            # Update the maximum length of the substring found so far
            max_length = max(max_length, i - start + 1)

        return max_length