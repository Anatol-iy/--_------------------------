import uuid
import networkx as nx
import matplotlib.pyplot as plt

class BinaryHeapNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_heap_edges(graph, heap, pos, parent_idx=0, x=0, y=0, layer=1):
    if parent_idx < len(heap):
        node = heap[parent_idx]
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if 2 * parent_idx + 1 < len(heap):
            left_idx = 2 * parent_idx + 1
            left_node = heap[left_idx]
            graph.add_edge(node.id, left_node.id)
            l = x - 1 / 2 ** layer
            pos[left_node.id] = (l, y - 1)
            l = add_heap_edges(graph, heap, pos, left_idx, x=l, y=y - 1, layer=layer + 1)
        if 2 * parent_idx + 2 < len(heap):
            right_idx = 2 * parent_idx + 2
            right_node = heap[right_idx]
            graph.add_edge(node.id, right_node.id)
            r = x + 1 / 2 ** layer
            pos[right_node.id] = (r, y - 1)
            r = add_heap_edges(graph, heap, pos, right_idx, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap):
    heap_graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    heap_graph = add_heap_edges(heap_graph, heap, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи
heap = [BinaryHeapNode(0), BinaryHeapNode(4), BinaryHeapNode(1), BinaryHeapNode(5), BinaryHeapNode(10), BinaryHeapNode(3)]

# Відображення бінарної купи
draw_heap(heap)
