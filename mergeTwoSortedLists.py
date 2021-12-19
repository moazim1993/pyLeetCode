
""""
# Leetcode 21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
> The number of nodes in both lists is in the range [0, 50].
> -100 <= Node.val <= 100
> Both l1 and l2 are sorted in non-decreasing order.

"""
def mergeTwoLists(l1, l2):
    l3 = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] <= l2[0]:
            #print('L1 : ',l1, l2, l3)
            l3.append(l1.pop(0))
        elif l1[0] > l2[0]:
            #print('L2 : ',l1, l2, l3)
            l3.append(l2.pop(0))
            
    if len(l1) == 0:
        l3 += l2
    elif len(l2) == 0:
        l3 += l1

    return(l3)
    
# testcase 1
l1 = [1,2,4]
l2 = [1,3,4]
#mergeTwoLists(l1,l2)

#testcase 2
l1 = []
l2 = []
#mergeTwoLists(l1,l2)

#testcase 3
l1 = []
l2 = [0]
#mergeTwoLists(l1,l2)


"""
instead of 2 lists we have list nodes
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

l1n1 = ListNode(4,None)
l1n2 = ListNode(2,l1n1)
l1n3 = ListNode(1,l1n2)
l1 = l1n3
l2n1 = ListNode(4,None)
l2n2 = ListNode(3,l2n1)
l2n3 = ListNode(1,l2n2)
l2 = l2n3


def showListNode(l1):
    l = []
    while l1.next:
        l.append(l1.val)
        l1 = l1.next
        
    l.append(l1.val)
    print(l) 


#showListNode(l1)
#showListNode(l2)


def mergeTwoListNodes(l1, l2):
    l3 = None
    showListNode(l1)
    showListNode(l2)
    
    while (l1 != None) or (l2 != None):
        if (l1.val <= l2.val) and not (l1 == None):
            print('L1 : ',l1, l2, l3)
            l3 = ListNode(l1.val,l3)
            l1 = l1.next
        elif l1.val > l2.val:
            #print('L2 : ',l1, l2, l3)
            l3 = ListNode(l2.val,l3)
            l2 = l2.next
        #breakpoint()
    """      
    if l1 == None:
        l3 += l2
    elif l2 == None:
        l3 += l1

    return(l3)
    """


res = mergeTwoListNodes(l1, l2)
showListNode(res)