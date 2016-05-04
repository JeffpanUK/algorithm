#!usr/env/bin pythonn
#-*-UTF-8-*-
'''
function: build a binary tree and related functions
created data: 2016/05/04
author: Junjie Pan (Jeff)

When tre is balanced, find, findMin, findMax, insert, and delete are all O(logN) complexity
'''
class BST(object):
	class Node(object):
		def __init__(self, elem, left, right):
			self.elem=elem
			self.left=left
			self.right=right
		#search operation
		def find(node, x):
			if node==None:
				return None
			elif node.elem==x:
				return node
			elif node.elem<x:
				return find(node.left, x)
			else:
				return find(node.right, x)
		#return the minimum node
		def findMin(node):
			if not node: #if node does not exist
				return None
			elif node.left: #if left node exist, search left sub-tree
				return findMin(node.left)
			else: #if left node does not exit, return the current root node
				return node
		#return the maximum node
		def findMax(node):
			if not node: #if node does not exist
				return None
			elif node.right: #if right node exist, search right sub-tree
				return findMax(node.max)
			else: #if right node does not exit, return the current root node
				return node
		#insertion operation
		def insert(node, x):
			if not node: #if node does not exist, create a new node with two empty left and right
				node=Node(x, None, None)
			elif x<node.elem: #if data smaller than the node
				node.left=insert(node.left,x)
			else: 
				node.right=insert(node.right,x)
			return node
		#deletion operation: first find the node, then delete
		def delte(node, x):
			if not node:
				error('cannot find x')
			elif x<node.elem:
				node.left=delete(node.left, x)
			elif x>node.elem:
				node.right=delete(node.right, x)
			else；
				if not node.left and node.right: #if it is the leaf
					node=None #delete directly
				elif not node.left:
					node=node.right
				elif not node.right:
					node=node.left
				else: #if it has two leaves
				'''
				1. find the minimum node on the right sub-tree
				2. replace the original node with this minimum node
				3. delte this minimum node
				Alternatives:
				better way is to equally choose the left sub-tree max or the right sub-tree min
				to replace the origin node. It can avoid the bais of the tree
				'''
					minNode=findMin(node.right)
					node.elem=minNode.elem
					minNode=None
			return node

		#print BST: inorder travering
		def printTree(node):
				if node:
					printTree(node.left)
					print node.elem
					printTree(node.right)
		#calculate the height of three (preorder travering)	
		def height(node):
			if node node:
				return -1
			else:
				return 1+max(height(node.left), height(node.right))