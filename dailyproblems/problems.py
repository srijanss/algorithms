"""
Daily Coding Problems
"""
from functools import reduce

class Node(object):
    def __init__(self, val, nextval=None):
        self.val = val
        self.nextval = nextval

    def traverse(self):
        nextval = self
        while nextval:
            print(nextval.val)
            nextval = nextval.nextval

class BinaryTreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def serialize(node):
    """
    converts tree of node objects to string
    """
    if not node:
        return '-'
    elif isinstance(node, BinaryTreeNode):
        return 'Node(' + node.val + ',' + serialize(node.left) + ',' + serialize(node.right) + ')'
    else:
        return node

def deserialize(nodestr):
    """
    converts to tree of node objects
    root,l-left,l-left.left,l-,r-,r-,right,l-,r-
    Node(root, Node(left, Node(left.left, -, -), -), Node(right, - , -))
    TODO: Change deserialize to recursive function
    # if 'Node' in nodestr:
    #     node = BinaryTreeNode(nodestr.split('(')[1])
    # elif '-' in nodestr:
    #     node = None
    # else:
    #     node = nodestr.split(',')[0] 
    """
    nodestr = nodestr.split(',')
    if 'Node' in nodestr[0]:
        node = BinaryTreeNode(nodestr[0].split('(')[1])
        if 'Node' in  nodestr[1]:
            node.left = BinaryTreeNode(nodestr[1].split('(')[1])
            if 'Node' in nodestr[2]:
                node.left.left = BinaryTreeNode(nodestr[2].split('(')[1])
            elif '-' in nodestr[2]:
                node.left.left = None
            else:
                node.left.left = nodestr[2].split(',')[0]
            if 'Node' in nodestr[3]:
                node.left.right = BinaryTreeNode(nodestr[2].split('(')[1])
            elif '-' in nodestr[3]:
                node.left.right = None
            else:
                node.left.right = nodestr[3].split(',')[0]
        elif '-' in nodestr[1]:
            node.left = None
        else:
            node.left = nodestr[1].split(',')[0]
        if 'Node' in  nodestr[4]:
            node.right = BinaryTreeNode(nodestr[4].split('(')[1])
            if 'Node' in nodestr[5]:
                node.right.left = BinaryTreeNode(nodestr[5].split('(')[1])
            elif '-' in nodestr[5]:
                node.right.left = None
            else:
                node.right.left = nodestr[5].split(',')[0]
            if 'Node' in nodestr[6]:
                node.right.right = BinaryTreeNode(nodestr[6].split('(')[1])
            elif '-' in nodestr[6]:
                node.right.right = None
            else:
                node.right.right = nodestr[6].split(',')[0]
        elif '-' in nodestr[4]:
            node.right = None
        else:
            node.right = nodestr[4].split(',')[0]
    elif '-' in nodestr[0]:
        node = None
    else:
        node = nodestr[0].split(',')[0]

    return node

    # if len(nodestr) == 3:
    #     return BinaryTreeNode(nodestr[0] if nodestr[0] != '-' else None, left=nodestr[1] if nodestr[1] != '-' else None, right=nodestr[2] if nodestr[2] != '-' else None)
    # else:
    #     return BinaryTreeNode(nodestr[0], left=deserialize(nodestr[1:]), right=deserialize(nodestr[2:]))

class Problems(object):
    """
    """
    def __init__(self):
        pass

    def day_one(self, arr, value):
        """
        [10, 2, 3, 4, 5, 7] and value = 17
        return true if sum of any two value equals value
        """
        for index, item in enumerate(arr):
            for nextindex, nextitem in enumerate(arr):
                if index != nextindex and item + nextitem == value:
                    return True
        return False

    def day_two(self, arr):
        """
        [1,2,3,4,5], result = [120, 60, 40, 30, 24]
        """
        # new_arr = []
        # for index, item in enumerate(arr):
        #     prod = 1
        #     for nextindex, nextitem in enumerate(arr):
        #         if index != nextindex:
        #             prod *= nextitem
        #     new_arr.append(prod)
        # return new_arr
        prod = reduce(lambda x, y: x * y, arr)
        return list(map(lambda x: prod//x, arr))

    def day_three(self):
        """
        Given the root to a binary tree, implement serialize(root),
        which serializes the tree into a string, and deserialize(s),
        which deserializes the string back into the tree.

        For example, given the following Node class

        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
            self.left = left
                self.right = right
        The following test should pass:

        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'
        """
        # node = BinaryTreeNode('root', 'left', 'right')
        node = BinaryTreeNode('root', BinaryTreeNode('left', BinaryTreeNode('left.left')), BinaryTreeNode('right'))
        return deserialize(serialize(node)).left.left.val
