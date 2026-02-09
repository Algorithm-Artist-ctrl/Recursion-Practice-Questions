class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.ans = []
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
    def inorderTraversal(self, root):
        self.ans = []
        self.inorder(root)
        return self.ans
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
print(sol.inorderTraversal(root))  