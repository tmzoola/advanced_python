# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr !=None:   #[None,4,5,6]
            nxt = curr.next  
            curr.next =prev 
            prev = curr
            curr = nxt
            
        return prev
    