"""
Завдання 2

Напишіть алгоритм (функцію), який знаходить найменше значення у
двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
from data import create_avl_tree

tree = create_avl_tree([1, 5, 2, 4]);

def sum_in_avl_tree(node):
    """
    Визначення суми без рекурсії
    """
    if not node:
        return None
    
    stack = [node]
    total = 0
    while stack:
        current = stack.pop()
        total += current.key
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return total

print("=== AVL Tree ===")
print(f"Input: {tree.input}")
print(tree)
sum = sum_in_avl_tree(tree)
print(f"Sum: {sum}")