# 单链表反转 

# Time complexity : O(n)O(n). Assume that nn is the list's length, the time complexity is O(n)O(n).
# Space complexity : O(1)O(1).
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            print(prev)
            
        return prev
