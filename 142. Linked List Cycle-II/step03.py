class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None
