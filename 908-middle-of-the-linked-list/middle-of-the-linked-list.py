# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        # Loop until the fast pointer reaches the end of the list.
        # The 'fast.next' check handles even-length lists.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    
        # When the loop ends, the slow pointer is at the middle node.
        return slow