class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BST():
    def addNode(self,root,value):
        newNode=Node(value)
        if root==None:
            return newNode
        if value<root.data:
            if root.left==None:
                root.left=newNode
            else:
                self.addNode(root.left,value)
        else:
            if root.right==None:
                root.right=newNode
            else:
                self.addNode(root.right,value)


    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data,end=", ")
        if root.right!=None:
            self.inorder(root.right)

    def preorder(self,root):
        print(root.data,end=", ")
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)

    def postorder(self,root):
        if root.left!=None:
            self.postorder(root.left)
        if root.right!=None:
            self.postorder(root.right)
        print(root.data,end=", ")

    #Implementation of Trees using Queues
    def level_order(self,root):
        q=[root]
        while len(q)!=0:
            ele=q.pop(0)
            print(ele.data,end=", ")
            if ele.left!=None:
                q.append(ele.left)
            if ele.right!=None:
                q.append(ele.right)


value=[16,9,25,4,15,83,8,18]
tree=BST()
root=None
root=tree.addNode(root,value[0])
print(root)
for i in range(1,len(value)):
    tree.addNode(root,value[i])
tree.inorder(root)
print()
tree.preorder(root)
print()
tree.postorder(root)
print()
tree.level_order(root)