# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sorted_arr=list()
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        def inordertravers(node):
            if node:
                inordertravers(node.left)
                self.sorted_arr.append(node.val)
                inordertravers(node.right)

        if not root:
            return False
        inordertravers(root)
        i=0
        j=len(self.sorted_arr)-1

        while i<j:
            if self.sorted_arr[i]+ self. sorted_arr[j]==k:
                return True
            elif self.sorted_arr[i]+self. sorted_arr[j] > k :
                j-=1
            else:
                i+=1
        return False


        