class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy=ListNode(0)
        current=dummy
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            
            total =val1 + val2 + carry
            carry=total//10
            current.next=ListNode(total%10)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next

# ---------- Create Linked Lists ----------

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


# ---------- Run Solution ----------

sol = Solution()
result = sol.addTwoNumbers(l1, l2)


# ---------- Print Output ----------

print("Result Linked List:")

while result:
    print(result.val, end=" -> ")
    result = result.next
print("none")