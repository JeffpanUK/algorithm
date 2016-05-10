'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Soulution:
	def binaryTreePath(self,root):
		if not root:
			return []
		#if no left and right leaves, return current root value
		if not root.left and not root.right:
			return [str(root.val)]

		leftPathToLeaf=self.binaryTreePath(root.left)
		rightPathToLeaf=self.binaryTreePath(root.right)

		left=[str(root.val)+('->'+i) for i in leftPathToLeaf]
		right=[str(root.val)+('->'+i) for i in rightPathToLeaf]

		return left+right