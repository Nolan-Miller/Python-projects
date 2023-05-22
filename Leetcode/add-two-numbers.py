'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

This solution beat 48.7% of run times (75 ms) and 24.35% of memory usages (16.3 MB)
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toString(self):
        curr = self
        out = ""
        while curr:
            out += str(curr.val)
            curr = curr.next
        return out


class Solution:
    #def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = temp = ListNode(0)
        carry = 0
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry = carry // 10
            curr = curr.next
        return temp.next

l1_input = input("Enter values for l1 (space-separated): ")
l1_values = list(map(int, l1_input.split()))
l1 = ListNode()
current_node = l1
for value in l1_values:
    current_node.next = ListNode(value)
    current_node = current_node.next

l2_input = input("Enter values for l2 (space-separated): ")
l2_values = list(map(int, l2_input.split()))
l2 = ListNode()
current_node = l2
for value in l2_values:
    current_node.next = ListNode(value)
    current_node = current_node.next

solution = Solution()
result = solution.addTwoNumbers(l1.next, l2.next)

print("Result:", result.toString())
