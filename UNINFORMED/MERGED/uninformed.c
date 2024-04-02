#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

#define MAX_VERTICES 100

typedef struct {
    int adjacency[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Graph;

void initializeGraph(Graph *g, int numVertices) {
    g->numVertices = numVertices;
    for (int i = 0; i < numVertices; ++i) {
        for (int j = 0; j < numVertices; ++j) {
            g->adjacency[i][j] = 0;
        }
    }
}

void addEdge(Graph *g, int src, int dest) {
    g->adjacency[src][dest] = 1;
}

bool depthLimitedSearch(Graph *g, int currentVertex, int targetVertex, int depth, bool visited[]) {
    printf("Analisis alur pencarian: Memeriksa simpul %d\n", currentVertex);

    if (currentVertex == targetVertex)
        return true;

    if (depth <= 0)
        return false;

    visited[currentVertex] = true;

    for (int i = 0; i < g->numVertices; ++i) {
        if (g->adjacency[currentVertex][i] && !visited[i]) {
            if (depthLimitedSearch(g, i, targetVertex, depth - 1, visited))
                return true;
        }
    }

    return false;
}

bool iterativeDeepeningSearch(Graph *g, int src, int dest, int maxDepth) {
    printf("Analisis alur pencarian: Memulai iterative deepening search\n");

    for (int depth = 1; depth <= maxDepth; ++depth) {
        bool visited[MAX_VERTICES] = {false};
        printf("Analisis alur pencarian: Memeriksa dengan kedalaman %d\n", depth);
        if (depthLimitedSearch(g, src, dest, depth, visited))
            return true;
    }
    return false;
}

bool findEvacuationPath(Graph *g, int src, int dest, int maxDepth) {
    printf("Analisis alur pencarian: Memulai depth limited search\n");
    bool visited[MAX_VERTICES] = {false};
    return depthLimitedSearch(g, src, dest, maxDepth, visited);
}

int main() {
    srand(time(NULL));

    while (true) {
        Graph g;
        
        int numVertices = rand() % MAX_VERTICES + 1;
        
        int numEdges = rand() % (numVertices * (numVertices - 1) / 2) + 1;

        initializeGraph(&g, numVertices);

        for (int i = 0; i < numEdges; ++i) {
            int src = rand() % numVertices;
            int dest = rand() % numVertices;
            addEdge(&g, src, dest);
        }

        int src = rand() % numVertices;
        int dest = rand() % numVertices;

        int maxDepth = rand() % numVertices + 1;

        printf("Input random:\n");
        printf("Jumlah simpul: %d\n", numVertices);
        printf("Jumlah edge: %d\n", numEdges);
        printf("Simpul awal: %d\n", src);
        printf("Simpul tujuan: %d\n", dest);
        printf("Kedalaman maksimum: %d\n", maxDepth);

        int choice;
        printf("Pilih metode pencarian (1 untuk iterative deepening, 2 untuk depth limited): ");
        scanf("%d", &choice);

        bool result = false;
        switch (choice) {
            case 1:
                result = iterativeDeepeningSearch(&g, src, dest, maxDepth);
                break;
            case 2:
                result = findEvacuationPath(&g, src, dest, maxDepth);
                break;
            default:
                printf("Pilihan tidak valid.\n");
                return 1;
        }

        if (result)
            printf("\nAda jalur evakuasi dengan kedalaman tidak lebih dari %d.\n", maxDepth);
        else
            printf("\nTidak ada jalur evakuasi dengan kedalaman tidak lebih dari %d.\n", maxDepth);

        printf("\nApakah Anda ingin melanjutkan (1 untuk ya, 0 untuk tidak)? ");
        scanf("%d", &choice);
        if (choice != 1)
            break;
    }

    return 0;
}
