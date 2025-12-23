"""
Завдання 2

Напишіть алгоритм (функцію), який знаходить найменше значення у
двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
from data import create_avl_tree

tree = create_avl_tree([1, 15, 10, 20, 8, 12, 8, 8, 9, 17, 25, 2]);

def find_min_in_avl_tree(node):
    """
    В самобалансуючому бінарному дереві пошуку, найменше значення буде знаходитися найглибше зліва.
    В циклі шукаємо найглибшу ліву ноду і повертаємо її.
    """
    if not node:
        return None
    while node.left:
        node = node.left
    return node

print("=== AVL Tree ===")
print(f"Input: {tree.input}")
print(tree)
found_min_node = find_min_in_avl_tree(tree)
print(f"Min: {found_min_node.key if found_min_node else 'Not found' }")