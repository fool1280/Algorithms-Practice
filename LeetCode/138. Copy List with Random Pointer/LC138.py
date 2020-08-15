class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def __init__(self):
        self.visitedNode = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        
        if head in self.visitedNode:
            return self.visitedNode[head]
        
        node = Node(head.val, None, None)
        self.visitedNode[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
    
res = Solution()
    