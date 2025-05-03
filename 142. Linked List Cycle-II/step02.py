class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        # サイクルが検出された時点でループ処理を終了
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # ループが存在せず上のwhileが終了した場合
        if fast.next is None or fast.next.next is None:
            return None
        
        # fastを最初に移動させてもう一度追いかけることでサイクルの開始点を検出。
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast