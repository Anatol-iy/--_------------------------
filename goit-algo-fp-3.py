# Імпорт бібліотек
import networkx as nx  # Для роботи з графами
import matplotlib.pyplot as plt  # Для візуалізації графів
from collections import deque

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    paths = []
    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                paths.append(path + [neighbor])
            else:
                queue.append((neighbor, path + [neighbor]))
    return paths

# Алгоритм Дейкстри для знаходження найкоротших шляхів в графі з вагами на ребрах
def dijkstra(graph, start):
    # Ініціалізуємо відстані та множину невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходимо вершину з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то завершуємо роботу
        if distances[current_vertex] == float('infinity'):
            break

        # Оновлюємо відстані до сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight.get('distance', 0)  # Отримуємо вагу ребра
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances



G_bus = nx.DiGraph() #направлений граф

# Добавляем вершины (остановки)
stops = ["Заклад швидкого харчування", "ТБ Хортиця", "Бул. Шевченка", "Вул. Нижньодніпровська", 
         "6 лікарня", "вул. Лермонтова", "Козак-палац", "Вознесенівський ринок", "Інститут",
         "5 лікарня", "БК Титан", "Управління патрульної поліції"]
G_bus.add_nodes_from(stops)


bus_routes = [
    ("Заклад швидкого харчування", "ТБ Хортиця", {"distance": 5}),  
    ("ТБ Хортиця", "Бул. Шевченка", {"distance": 3}), 
    ("Бул. Шевченка", "Вул. Нижньодніпровська", {"distance": 6}),  
    ("Вул. Нижньодніпровська", "6 лікарня", {"distance": 2}),  
    ("6 лікарня", "вул. Лермонтова", {"distance": 5}),
    ("вул. Лермонтова", "Козак-палац", {"distance": 1}),
    ("Козак-палац", "Вознесенівський ринок", {"distance": 4}),
    ("Вознесенівський ринок", "Інститут", {"distance": 3}),
    ("Інститут", "5 лікарня", {"distance": 7}),
    ("5 лікарня", "БК Титан", {"distance": 6}),
    ("БК Титан", "Управління патрульної поліції", {"distance": 3}),        
]

G_bus.add_edges_from(bus_routes)
G_bus.add_edge("6 лікарня", "Інститут", distance=3)
G_bus.add_edge("6 лікарня", "Вознесенівський ринок", distance=2)
G_bus.add_edge("Заклад швидкого харчування", "вул. Лермонтова", distance=8)
G_bus.add_edge("Заклад швидкого харчування", "БК Титан", distance=20)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G_bus)
nx.draw(G_bus, pos, with_labels=True, node_size=2000, node_color="lightyellow", font_size=12, font_weight="bold", arrowsize=30)
edge_labels = {(i, j): f"{attr['distance']} км" for i, j, attr in G_bus.edges(data=True)}
nx.draw_networkx_edge_labels(G_bus, pos, edge_labels=edge_labels, font_color='red')
plt.title("Доставка заказів з закладу швидкого харчування")
plt.show()


print("Количество вершин:", G_bus.number_of_nodes())
print("Количество рёбер:", G_bus.number_of_edges())
print("Список вершин:", list(G_bus.nodes()))
print("Степень вершин:")
for node in G_bus.nodes():
    print(f"Вершина {node}:", G_bus.degree(node))


# Виклик алгоритму DFS для знаходження шляху між двома вузлами
start_node = "Заклад швидкого харчування"
end_node = "Управління патрульної поліції"
dfs_paths = dfs(G_bus, start_node, end_node)
print("Шляхи DFS між", start_node, "і", end_node, ":", dfs_paths)

# Виклик алгоритму BFS для знаходження шляху між двома вузлами
bfs_paths = bfs(G_bus, start_node, end_node)
print("Шляхи BFS між", start_node, "і", end_node, ":", bfs_paths)

# Виклик алгоритму Дейкстри для знаходження найкоротшого шляху в графі
start_node_dijkstra = "Заклад швидкого харчування"
dijkstra_shortest_paths = dijkstra(G_bus, start_node_dijkstra)
print("Найкоротші відстані від", start_node_dijkstra, "до кожної вершини:", dijkstra_shortest_paths)