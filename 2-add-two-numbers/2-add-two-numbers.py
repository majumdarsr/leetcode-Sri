# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = 0
        l2_num = 0
        head1 = l1
        head2 = l2
        count1 = 0
        count2 = 0
        # as long as head.next is a ListNode
        while(head1 != None or head2 != None):
            if head1 != None:
                l1_num += head1.val * (10 ** count1)
                head1 = head1.next
                count1 += 1
            if head2 != None:
                l2_num += head2.val * (10 ** count2)
                head2 = head2.next
                count2 += 1
                
        num = l1_num + l2_num
                
        head = l3 = ListNode(val = num % 10)
        num = num // 10
        while num != 0:
            l3.next = ListNode(val = num % 10)
            l3 = l3.next
            num = num // 10
        
        return head


        
        
            
            
        