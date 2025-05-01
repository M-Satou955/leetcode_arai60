# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 重複を削除する場合先頭の削除ができないので先頭に0を挿入
        dummy_list = ListNode(0, head)
        pred = dummy_list
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                while head.next is not None and head.val == head.next.val:
                    head = head.next
                # ポインターの示す先を重複を削除したheadに
                dummy_list.next = head.next
            else:
                dummy_list = dummy_list.next
            head = head.next
        return pred.next