class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # Initialize two pointers for nums1 and nums2
        p1, p2 = m - 1, n - 1
        
        # Start from the end of nums1 and move elements to the end
        # while comparing and merging elements from nums2
        for i in range(m + n - 1, -1, -1):
            if p2 < 0:
                break  # All elements from nums2 are merged
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1