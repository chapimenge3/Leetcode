# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = 0
        s = l1.val + l2.val
        if s > 9:
            s = int(str(s)[-1])
            q = 1
        res = ListNode(s)
        prev = res
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        while l1 or l2:
            s = 0
            if l1 is None and l2:
                s = l2.val + q
            elif l1 and l2 is None:
                s = l1.val + q
            else:
                s = l1.val + l2.val + q
            
            if s > 9:
                s = int(str(s)[-1])
                q = 1
            else:
                q = 0
            
            rs = ListNode(s)
            prev.next = rs
            prev = rs
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None



        
        if q :
            rs = ListNode(1)
            prev.next = rs
        
        return res





