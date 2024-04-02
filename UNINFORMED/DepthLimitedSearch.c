#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

#define MAX_VERTICES 100

typedef struct
{
    int adjacency[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Graph;

void initializeGraph(Graph *g, int numVertices)
{
    g->numVertices = numVertices;
    for (int i = 0; i < numVertices; ++i)
    {
        for (int j = 0; j < numVertices; ++j)
        {
            g->adjacency[i][j] = 0;
        }
    }
}

void addEdge(Graph *g, int src, int dest)
{
    g->adjacency[src][dest] = 1;
}

bool depthLimitedSearch(Graph *g, int currentVertex, int targetVertex, int depth, bool visited[])
{
    if (currentVertex == targetVertex)
        return true;

    if (depth <= 0)
        return false;

    visited[currentVertex] = true;

    for (int i = 0; i < g->numVertices; ++i)
    {
        if (g->adjacency[currentVertex][i] && !visited[i])
        {
            if (depthLimitedSearch(g, i, targetVertex, depth - 1, visited))
                return true;
        }
    }

    return false;
}

bool findEvacuationPath(Graph *g, int src, int dest, int maxDepth)
{
    bool visited[MAX_VERTICES] = {false};
    return depthLimitedSearch(g, src, dest, maxDepth, visited);
}

int main()
{
    // initialisasi generate nomor secara acak
    srand(time(NULL));

    Graph g;
    // jumlah simpul antara 1 dan MAX_VERTICES
    int numVertices = rand() % MAX_VERTICES + 1;
    // jumlah edge antara 1 dan (numVertices*(numVertices-1))/2
    int numEdges = rand() % (numVertices * (numVertices - 1) / 2) + 1;

    initializeGraph(&g, numVertices);

    // menambahkan edge secara acak
    for (int i = 0; i < numEdges; ++i)
    {
        int src = rand() % numVertices;
        int dest = rand() % numVertices;
        addEdge(&g, src, dest);
    }

    int src = rand() % numVertices;
    int dest = rand() % numVertices;
    // kedalaman maksimum antara 1 dan numVertices
    int maxDepth = rand() % numVertices + 1;

    printf("Input random:\n");
    printf("Jumlah simpul: %d\n", numVertices);
    printf("Jumlah edge: %d\n", numEdges);
    printf("Simpul awal: %d\n", src);
    printf("Simpul tujuan: %d\n", dest);
    printf("Kedalaman maksimum: %d\n", maxDepth);

    if (findEvacuationPath(&g, src, dest, maxDepth))
        printf("\nAda jalur evakuasi dengan kedalaman tidak lebih dari %d.\n", maxDepth);
    else
        printf("\nTidak ada jalur evakuasi dengan kedalaman tidak lebih dari %d.\n", maxDepth);

    return 0;
}
