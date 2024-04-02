import heapq

class Node:
    def __init__(self, state, g_rute=0, h_rute=0):
        self.state = state
        self.g_rute = g_rute  # rute dari simpul awal
        self.h_rute = h_rute  # rute heuristik
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

def weighted_a_star(graph, start, goal, weight):
    open_set = []
    closed_set = set()
    came_from = {}  
    rute_so_far = {start: 0} 
    
    start_node = Node(start)
    start_node.g_rute = 0
    start_node.h_rute = graph.heuristic[start]  # Panggil heuristic yang sudah diperbaiki
    start_node.f_rute = start_node.g_rute + weight * start_node.h_rute

    heapq.heappush(open_set, start_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)
        
        if current_node.state == goal:
            path = reconstruct_path(came_from, start, goal)  # Rekonstruksi jalur dari titik awal ke titik tujuan
            return path
        
        closed_set.add(current_node.state)
        
        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue
            
            g_rute = current_node.g_rute + 1  
            h_rute = graph.heuristic[neighbor]
            f_rute = g_rute + weight * h_rute
            
            if neighbor not in rute_so_far or g_rute < rute_so_far[neighbor]:
                rute_so_far[neighbor] = g_rute
                heapq.heappush(open_set, Node(neighbor, g_rute, h_rute))
                came_from[neighbor] = current_node.state  # Simpan jalur yang diambil
    
    return None

def reconstruct_path(came_from, start, goal):
    current_node = goal
    path = [current_node]
    while current_node != start:
        current_node = came_from[current_node]
        path.append(current_node)
    return ' -> '.join(path[::-1])  # Balikkan jalur karena jalur direkonstruksi dari tujuan ke awal

if __name__ == "__main__":
    heuristic = {
        'Semarang': 9,
        'Bandung': 4,
        'Jogja': 2,
        'Jakarta': 5,
        'Malang': 3,
        'Surabaya': 7,
        'Banten': 0
    }

    graph_data = {
        'Surabaya': {'Semarang', 'Malang'},
        'Semarang': {'Bandung', 'Jogja'},
        'Bandung': {'Jakarta'},
        'Jogja': {'Banten'},
        'Jakarta': {'Banten'},
        'Malang': {'Jakarta'},
        'Banten': set()  # Tambahkan 'Banten' ke graf dengan tetangga kosong
    }

    graph = Graph(graph_data, heuristic)
    start = 'Surabaya'
    goal = 'Banten'
    weight = 2  # Weight parameter for weighted A*
    
    result = weighted_a_star(graph, start, goal, weight)
    
    if result:
        print("Rute ditemukan")
        print("Rute:", result)
    else:
        print("Tidak ada rute yang ditemukan.")
