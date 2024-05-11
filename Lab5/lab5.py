import numpy as np
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

def search(root, val):
    if root is None or root.val == val:
        return root
    if root.val < val:
        return search(root.right, val)
    return search(root.left, val)

def find_max(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.val

def print_tree(root, level=0, prefix="Root:"):
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--")
            print_tree(root.right, level + 1, "R--")

def tree_height(root):
    if root is None:
        return -1  # Повертаємо -1, оскільки висота порожнього дерева -1
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        
        # Повертаємо максимум з висот лівого та правого піддерева, додаючи 1 для поточного вузла
        return max(left_height, right_height) + 1
    
def printTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.left,level+1,x-seg,'l'))
            q.append((node.right,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].val)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)   


# Приклад використання
if __name__ == "__main__":
    root = None
    nums = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    random_list = np.random.randint(0, 100, size=20)
    for num in random_list:
        root = insert(root, num)
    printTree(root)

