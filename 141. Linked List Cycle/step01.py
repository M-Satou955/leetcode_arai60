# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()
        while head:
            if head in visited_node:
                return True
            visited_node.add(head)
            head = head.next
        return False