class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            if len(path) == k:
                results_list.append(path[:])  # Make a copy of the current combination
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        results_list = []
        backtrack(1, [])
        return results_list