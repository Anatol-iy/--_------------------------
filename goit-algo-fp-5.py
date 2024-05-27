import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def heapify_tree(node):
    if node is None:
        return

    # Рекурсивно викликаємо heapify_tree для лівого та правого піддерева
    heapify_tree(node.left)
    heapify_tree(node.right)

    # Викликаємо процедуру heapify для поточного вузла
    heapify_node(node)


def heapify_node(node):
    if node is None:
        return

    # Перевіряємо, чи поточний вузол менший за свого лівого дочірнього вузла,
    # та якщо так, міняємо їх місцями
    if node.left is not None and node.left.val > node.val:
        node.val, node.left.val = node.left.val, node.val
        # Рекурсивно викликаємо heapify_node для лівого піддерева
        heapify_node(node.left)

    # Перевіряємо, чи поточний вузол менший за свого правого дочірнього вузла,
    # та якщо так, міняємо їх місцями
    if node.right is not None and node.right.val > node.val:
        node.val, node.right.val = node.right.val, node.val
        # Рекурсивно викликаємо heapify_node для правого піддерева
        heapify_node(node.right)


def get_color(index):
    # Генерація послідовності кольорів від темного до світлого
    # Генеруємо відтінок в 16-ковому форматі
    intensity = hex(20 * index)[2:].zfill(2)
    color = '#' + intensity * 3  # Використовуємо один відтінок для всіх компонентів RGB
    return color


def dfs_recursive(node, visited=None, colors=None):
    if visited is None:
        visited = set()
    if colors is None:
        colors = {}
    if node is None:
        return
    if node not in visited:
        node.color = get_color(len(colors))
        colors[node.id] = node.color
    visited.add(node)
    print(node, end=' ')  # Відвідуємо вершину
    for neighbor in (node.left, node.right):
        if neighbor not in visited:
            dfs_recursive(neighbor, visited, colors)


def bfs_recursive(root):
    visited, queue = set(), [root]
    colors = {}
    step = 0

    while queue:
        noda = queue.pop(0)
        print("Noda ", noda.val)
        if noda not in visited:
            visited.add(noda)
            noda.color = get_color(step)
            colors[noda.id] = noda.color
            step += 1
            if noda.left:
                queue.append(noda.left)
            if noda.right:
                queue.append(noda.right)


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Отримуємо кольори вершин з об'єктів класу Node
    colors = [data['color'] for node_id, data in tree.nodes(data=True)]
    labels = {node_id: data['label']
              for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
heapify_tree(root)
# dfs_recursive(root)
bfs_recursive(root)
draw_tree(root)