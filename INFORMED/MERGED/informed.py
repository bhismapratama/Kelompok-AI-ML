import random
import heapq

class Node:
    def __init__(self, state, g_rute=0, h_rute=0):
        self.state = state
        self.g_rute = g_rute
        self.h_rute = h_rute
        self.f_rute = g_rute + h_rute
        self.parent = None

    def __lt__(self, other):
        return self.f_rute < other.f_rute

class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def get_neighbors(self, node):
        return self.graph[node]

def generate_heuristic(locations):
    heuristic = {}
    for location in locations:
        heuristic[location] = random.randint(0, 10)
    return heuristic

def generate_random_graph(locations):
    graph = {}
    for location in locations:
        num_neighbors = random.randint(0, len(locations) // 2)
        neighbors = random.sample(locations, num_neighbors)
        graph[location] = set(neighbors)
    return graph

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()
    came_from = {}
    rute_so_far = {start: 0}
    explored_nodes = 0

    start_node = Node(start)
    start_node.g_rute = 0
    start_node.h_rute = heuristic[start]
    start_node.f_rute = start_node.g_rute + start_node.h_rute

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        explored_nodes += 1

        if current_node.state == goal:
            path = reconstruct_path(came_from, start, goal)
            return path, explored_nodes, len(closed_set)

        closed_set.add(current_node.state)

        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            g_rute = current_node.g_rute + 1
            h_rute = heuristic[neighbor]
            f_rute = g_rute + h_rute

            if neighbor not in rute_so_far or g_rute < rute_so_far[neighbor]:
                rute_so_far[neighbor] = g_rute
                heapq.heappush(open_set, Node(neighbor, g_rute, h_rute))
                came_from[neighbor] = current_node.state

    return None, explored_nodes, len(closed_set)

def weighted_a_star_search(graph, start, goal, heuristic, weight):
    open_set = []
    closed_set = set()
    came_from = {}
    rute_so_far = {start: 0}
    explored_nodes = 0

    start_node = Node(start)
    start_node.g_rute = 0
    start_node.h_rute = heuristic[start]
    start_node.f_rute = start_node.g_rute + weight * start_node.h_rute

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        explored_nodes += 1

        if current_node.state == goal:
            path = reconstruct_path(came_from, start, goal)
            return path, explored_nodes, len(closed_set)

        closed_set.add(current_node.state)

        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            g_rute = current_node.g_rute + 1
            h_rute = heuristic[neighbor]
            f_rute = g_rute + weight * h_rute

            if neighbor not in rute_so_far or g_rute < rute_so_far[neighbor]:
                rute_so_far[neighbor] = g_rute
                heapq.heappush(open_set, Node(neighbor, g_rute, h_rute))
                came_from[neighbor] = current_node.state

    return None, explored_nodes, len(closed_set)

def greedy_search(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()
    came_from = {}
    explored_nodes = 0

    start_node = Node(start)
    start_node.h_rute = heuristic[start]

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        explored_nodes += 1

        if current_node.state == goal:
            path = reconstruct_path(came_from, start, goal)
            return path, explored_nodes, len(closed_set)

        closed_set.add(current_node.state)

        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            heapq.heappush(open_set, Node(neighbor, h_rute=heuristic[neighbor]))
            came_from[neighbor] = current_node.state

    return None, explored_nodes, len(closed_set)

def reconstruct_path(came_from, start, goal):
    current_node = goal
    path = [current_node]
    while current_node != start:
        current_node = came_from[current_node]
        path.append(current_node)
    return ' -> '.join(path[::-1])

if __name__ == "__main__":
    while True:
        locations = ['Semarang', 'Bandung', 'Jogja', 'Jakarta', 'Malang', 'Surabaya', 'Banten']

        heuristic = generate_heuristic(locations)
        graph_data = generate_random_graph(locations)

        print(" ")
        print("=============================================================")
        print(" ")
        print("Heuristik acak:", heuristic)
        print("Graf acak:", graph_data)

        graph = Graph(graph_data, heuristic)
        start = 'Surabaya'
        goal = 'Banten'

        print("\nPilih Algoritma:")
        print("1. A*")
        print("2. Weighted A*")
        print("3. Greedy")
        print("4. Keluar")
        choice = int(input("Masukkan pilihan Anda (1/2/3/4): "))

        if choice == 1:
            result, explored_nodes, closed_nodes = a_star_search(graph, start, goal, heuristic)
            algorithm_name = "A*"
        elif choice == 2:
            weight = float(input("Masukkan nilai bobot (float): "))
            result, explored_nodes, closed_nodes = weighted_a_star_search(graph, start, goal, heuristic, weight)
            algorithm_name = "Weighted A*"
        elif choice == 3:
            result, explored_nodes, closed_nodes = greedy_search(graph, start, goal, heuristic)
            algorithm_name = "Greedy"
        elif choice == 4:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
            continue

        if result:
            print("\nRute ditemukan")
            print("Rute:", result)
        else:
            print("Tidak ada rute yang ditemukan.")
            
        print("Analisis pencarian:")
        print("Nama Algoritma:", algorithm_name)
        print("Jumlah simpul yang dieksplorasi:", explored_nodes)
        print("Jumlah simpul yang dipilih untuk solusi:", closed_nodes)
