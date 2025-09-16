#- Time complexity:
#<!-- $$O(n)$$ -->

#- Space complexity:
#<!-- $$O(1)$$ -->

# Code
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
	    
        if not head or k==0:
            return head

        ln=1
        tail=head
        while tail.next:
            tail = tail.next
            ln+=1
            
        tail.next = head
        
        # Calculate the effective number of rotations
        k = k % ln
        
        # Find the new tail: ln - k steps from the original head
        new_tail = head
        for _ in range(ln - k - 1):
            new_tail = new_tail.next
        
        # Find the new head
        new_head = new_tail.next
        
        # Break the circular connection
        new_tail.next = None
        
        return new_head
