import numpy as np

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def search(root, key):
    """
    Searching value in binary tree
    """
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)     

def show_searched_val(root, key):
    """
    Searching value in binary tree and showing binary tree
    """
    return print_tree(root, searched_value=key)

def find_max(root):
    """
    Searching max value in binary tree
    """
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.value

def show_max(root):
    """
    Searching max value in binary tree and showing binary tree
    """
    key = find_max(root)
    return print_tree(root, searched_value=key)

def insert(root, value):
    """
    Inserting value into binary tree
    """
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def print_tree(root, is_left=None, prefix='', has_right_child=True, has_left_child=True, searched_value=None):
    """
    Demonstating binary tree
    """
    if searched_value:
        if root.left:
            print_tree(root.left, True, prefix + ('    ' if has_right_child else '|   '), has_right_child=True, has_left_child=False, searched_value=searched_value)

        if is_left == True:
            if root.left:
                print(prefix + '    |   ')
            else:
                print(prefix )
            if root.value == searched_value:
                print(prefix +  '┌──>' + str(root.value) + ' ')
            else:
                print(prefix +  '┌──>' + str(root.value))

        elif is_left == False:
            if root.value == searched_value:
                print(prefix  + '└──>' + str(root.value) + ' Searched')
            else:
                print(prefix  + '└──>' + str(root.value))
            if root.right:
                print(prefix + '    |   ')
            else:
                print(prefix )

        else:
            if root.value == searched_value:
                print('|── ' + str(root.value) + ' Searched')
            else:
                print('|── ' + str(root.value))

        if root.right:
            print_tree(root.right, False, prefix + ('    ' if has_left_child else '|   '), has_right_child=False, has_left_child=True, searched_value=searched_value)
    else:
        if root.left:
            print_tree(root.left, True, prefix + ('    ' if has_right_child else '|   '), has_right_child=True, has_left_child=False)

        if is_left == True:
            if root.left:
                print(prefix + '    |   ')
            else:
                print(prefix )
            print(prefix +  '┌──>' + str(root.value))

        elif is_left == False:
            print(prefix  + '└──>' + str(root.value))
            if root.right:
                print(prefix + '    |   ')
            else:
                print(prefix )

        else:
            print('|── ' + str(root.value))

        if root.right:
            print_tree(root.right, False, prefix + ('    ' if has_left_child else '|   '), has_right_child=False, has_left_child=True)


if __name__ == "__main__":
    root = None
    nums = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    random_list = np.random.randint(0, 100, size=20)
    for num in nums:
        root = insert(root, num)
    


    
