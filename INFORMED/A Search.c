#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>

#define V 6

int minCost(int cost[], bool visited[])
{
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (visited[v] == false && cost[v] < min)
            min = cost[v], min_index = v;
    return min_index;
}

void printPath(int parent[], int j)
{
    if (parent[j] == -1)
        return;
    printPath(parent, parent[j]);
    printf(" -> %d ", j);
}

void printSolution(int cost[], int parent[], int src, int dest)
{
    printf("Path from %d to %d: %d", src, dest, src);
    printPath(parent, dest);
    printf("\nTotal Cost: %d\n", cost[dest]);
}

void aStarSearch(int graph[V][V], int src, int dest, int heuristic[])
{
    int parent[V];
    bool visited[V];
    int cost[V];
    for (int i = 0; i < V; i++)
    {
        parent[src] = -1;
        visited[i] = false;
        cost[i] = INT_MAX;
    }
    cost[src] = 0;
    for (int count = 0; count < V - 1; count++)
    {
        int u = minCost(cost, visited);
        visited[u] = true;
        for (int v = 0; v < V; v++)
        {
            if (!visited[v] && graph[u][v] && cost[u] + graph[u][v] + heuristic[v] < cost[v])
            {
                parent[v] = u;
                cost[v] = cost[u] + graph[u][v] + heuristic[v];
            }
        }
    }
    printSolution(cost, parent, src, dest);
}

int main()
{
    int graph[V][V];
    printf("Masukkan biaya perjalanan antar-stasiun:\n");
    int inputCost;
    scanf("%d", &inputCost);

    srand(time(NULL));

    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            if (i != j)
            {
                graph[i][j] = rand() % inputCost + 1;
            }
            else
            {
                graph[i][j] = 0;
            }
        }
    }

    int heuristic[V];
    printf("Nilai heuristik untuk setiap stasiun (acak):\n");
    for (int i = 0; i < V; i++)
    {
        heuristic[i] = rand() % 10;
        printf("Heuristik pada stasiun %d: %d\n", i, heuristic[i]);
    }

    int src, dest;
    printf("Masukkan stasiun awal (nomor): ");
    if (scanf("%d", &src) != 1 || src < 0 || src >= V)
    {
        printf("Input tidak valid.\n");
        return 1;
    }
    printf("Masukkan stasiun tujuan (nomor): ");
    if (scanf("%d", &dest) != 1 || dest < 0 || dest >= V)
    {
        printf("Input tidak valid.\n");
        return 1;
    }
    aStarSearch(graph, src, dest, heuristic);
    return 0;
}
