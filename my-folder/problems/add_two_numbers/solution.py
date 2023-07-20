# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # Dummy node to simplify the code
        curr = dummy  # Pointer to the current node
        carry = 0  # Carry digit

        while l1 or l2 or carry:
            # Calculate the sum of current digits and carry
            sum_val = carry

            # If l1 is not None, add its value to sum_val
            if l1:
                sum_val += l1.val
                l1 = l1.next

            # If l2 is not None, add its value to sum_val
            if l2:
                sum_val += l2.val
                l2 = l2.next

        # Update the carry and create a new node for the sum_val
            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next

        return dummy.next