from queue import PriorityQueue

def greedy_search(graph, start, goal):
    frontier = PriorityQueue() 
    frontier.put(start, 0) 
    explored = set()  
    parent = {}  # Untuk melacak rute yang diambil
    
    while not frontier.empty():
        current_node = frontier.get() 
        
        if current_node == goal:
            print("Simpul tujuan sudah ditemukan!")
            print("Rute terpendek:", reconstruct_path(parent, start, goal))
            return True  
        
        explored.add(current_node)  
        
        for neighbor in graph[current_node]:
            if neighbor not in explored:
                parent[neighbor] = current_node
                priority = heuristic[neighbor]
                frontier.put(neighbor, priority)
        
    print("Simpul tujuan tidak ditemukan!")
    return False  

def reconstruct_path(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return ' -> '.join(path[::-1])

# Daftar heuristik untuk setiap simpul
heuristic = {
    'stasiun_semarang': 9,
    'stasiun_bandung': 4,
    'stasiun_jogja': 2,
    'stasiun_jakarta': 5,
    'stasiun_malang': 3,
    'stasiun_surabaya': 7,
    'stasiun_banten': 0
}

# Graf (dalam bentuk daftar kejadian)
graph = {
    'stasiun_surabaya': {'stasiun_semarang', 'stasiun_malang'},
    'stasiun_semarang': {'stasiun_bandung', 'stasiun_jogja'},
    'stasiun_bandung': {'stasiun_jakarta'},
    'stasiun_jogja': {'stasiun_banten'},
    'stasiun_jakarta': {'stasiun_banten'},
    'stasiun_malang': {'stasiun_jakarta'},
    'stasiun_banten': set()  # Tambahkan 'stasiun_banten' ke graf dengan tetangga kosong
}

# Titik awal dan tujuan
start_node = 'stasiun_surabaya'
goal_node = 'stasiun_banten'

# Panggil fungsi greedy search
greedy_search(graph, start_node, goal_node)
