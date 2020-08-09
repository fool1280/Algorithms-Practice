from typing import List
   
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = dummy = ListNode()
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            dummy.next = ListNode(x)
            dummy = dummy.next
        return head.next
