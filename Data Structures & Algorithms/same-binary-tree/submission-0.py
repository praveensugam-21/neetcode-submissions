# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root, lst):
            if not root:
                lst.append(None)   # Important to preserve structure
                return

            lst.append(root.val)
            dfs(root.left, lst)
            dfs(root.right, lst)

        list1 = []
        list2 = []

        dfs(p, list1)
        dfs(q, list2)

        return list1 == list2