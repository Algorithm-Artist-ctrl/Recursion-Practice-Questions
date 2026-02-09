class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ans = []

    def preorder(self, root):
        if root is None:
            return
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
print(sol.preorderTraversal(root))  
