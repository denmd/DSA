https://leetcode.com/problems/rotate-list/description/

- First we find the length of linked list and tail pointer .
- Tail pointer is connect to head because k node rotate means last k node is indirectly connect with head.
- Traverse the n-k node.
- n-k+1 node is declare to newHead and n-k next pointer assign NULL pointer.
return newHead.