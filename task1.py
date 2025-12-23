"""
Завдання 1
Напишіть алгоритм (функцію), який знаходить найбільше значення 
у двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
from data import create_binary_tree

binary_tree = create_binary_tree([15, 10, 20, 8, 12, 8, 8, 9, 17, 25]);

def find_max_in_binary_tree(node):
    """
    В бінарному дереві максимальний елемент знаходится в самій правій частині,
    тому, в циклі йдемо до нього і повертаємо найглибший правий елемент
    """
    if not node:
        return None
    while node.right:
        node = node.right
    return node

print("=== Binary Tree ===")
print(f"Input: {binary_tree.input}")
print(binary_tree)
found_max_node = find_max_in_binary_tree(binary_tree)
print(f"Max: {found_max_node.key if found_max_node else 'Not found' }")