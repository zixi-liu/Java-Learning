# 链表中环的检测

#Time complexity : O(n). We visit each of the nn elements in the list at most once. Adding a node to the hash table costs only O(1) time.
#Space complexity: O(n). The space depends on the number of elements added to the hash table, which contains at most nn elements.

# Use a Hash Set
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
      
# Use a Floyd's Cycle Finding Algorithm

# 设序列为A[n]，且从A[i]开始，对于任意m>=i有A[m+T]=A[m]，其中T>=1。我们只需要证明存在k，使得A[2k] = A[k]即可。任取一个使得uT>=i的u，令k=uT，则有A[2uT] = A[uT + uT] = A[uT + (u-1)T] = ... = A[uT]，即A[2k] = A[k]，命题得证
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
