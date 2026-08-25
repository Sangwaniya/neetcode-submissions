# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        d1, d2  = self.dfs(root)
        return max(d1, d2)
    def dfs(self, root):
        if not root:
            return [0, 0]
        
        dl1, dl2  =  self.dfs(root.left)
        
        dr1, dr2 = self.dfs(root.right)
        skip = max(dl1, dl2)+max(dr2, dr1)
        nskip = root.val+dl2+dr2
        return nskip, skip

