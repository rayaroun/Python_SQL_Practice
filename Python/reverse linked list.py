"""

Print a linked list in reverse using existing print and getNext fucntions for the linked list

"""

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        st = []
        while head != None:
            st.append(head)
            head = head.getNext()
        while st:
            st.pop().printValue()