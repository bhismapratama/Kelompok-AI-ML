import time

# in case merupakan jumlah stasiun yang ada
V = 6

def min_cost(cost, visited):

    # initialisasi biaya minimum
    min_val = float('inf') 
    # initialisasi index minimum
    min_index = -1
    for v in range(V):
        if not visited[v] and cost[v] < min_val:
            min_val = cost[v]
            min_index = v
    return min_index

def print_path(parent, j):
    if parent[j] == -1:
        return
    # rekursif mencetak jalur
    print_path(parent, parent[j])
    print(" ->", j, end='')

def print_solution(cost, parent, src, dest):
    # fungsi untuk mencetak jalur yang ditemukan dari stasiun awal ke stasiun tujuan, beserta total biaya perjalanan.
    print("Path from", src, "to", dest, ":", src, end='')
    print_path(parent, dest)
    print("\nTotal Cost:", cost[dest])

def a_star_search(graph, src, dest, heuristic):
    # array untuk menyimpan orang tua dari setiap stasiun yang dikunjungi.
    parent = [-1] * V
    # array untuk menandai stasiun yang telah dikunjungi.
    visited = [False] * V
    # array untuk menyimpan biaya terpendek dari stasiun awal ke setiap stasiun.
    cost = [float('inf')] * V

    # karan source awal adalah stasiun awal, jadi tidak ada biaya
    cost[src] = 0

    for _ in range(V - 1):
        u = min_cost(cost, visited)
        visited[u] = True
        for v in range(V):
            if not visited[v] and graph[u][v] and cost[u] + graph[u][v] + heuristic[v] < cost[v]:
                parent[v] = u
                cost[v] = cost[u] + graph[u][v] + heuristic[v]

    print_solution(cost, parent, src, dest)

def main():
    graph = [[0] * V for _ in range(V)]
    print("Masukkan biaya perjalanan antar-stasiun:")
    input_cost = int(input())

    for i in range(V):
        for j in range(V):
            if i != j:
                graph[i][j] = (i + j + 1) % input_cost + 1
            else:
                graph[i][j] = 0

    heuristic = []
    print("Nilai heuristik untuk setiap stasiun (acak):")
    for i in range(V):
        heuristic.append((i * 3) % 10)
        print("Heuristik pada stasiun", i, ":", heuristic[i])

    src = int(input("Masukkan stasiun awal (nomor): "))
    if src < 0 or src >= V:
        print("Input tidak valid.")
        return

    dest = int(input("Masukkan stasiun tujuan (nomor): "))
    if dest < 0 or dest >= V:
        print("Input tidak valid.")
        return

    a_star_search(graph, src, dest, heuristic)

if __name__ == "__main__":
    main()
