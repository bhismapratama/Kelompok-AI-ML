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
    printf("Menelusuri langkah: %d\n", currentVertex);

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
    printf("Memulai pencarian dari simpul: %d\n", src);

    for (int depth = 1; depth <= maxDepth; ++depth) {
        bool visited[MAX_VERTICES] = {false};
        printf("Pencarian dengan batas: %d\n", depth);
        if (depthLimitedSearch(g, src, dest, depth, visited)) {
            printf("Jalur evakuasi ditemukan dengan batas tidak lebih dari %d.\n", depth);
            return true;
        }
    }
    printf("Tidak ditemukan jalur evakuasi dengan batas tidak lebih dari %d.\n", maxDepth);
    return false;
}

bool findEvacuationPath(Graph *g, int src, int dest, int maxDepth) {
    printf("Memulai pencarian evakuasi...\n");
    bool visited[MAX_VERTICES] = {false};
    if (depthLimitedSearch(g, src, dest, maxDepth, visited)) {
        printf("Jalur evakuasi ditemukan dengan batas tidak lebih dari %d.\n", maxDepth);
        return true;
    }
    printf("Tidak ditemukan jalur evakuasi dengan batas tidak lebih dari %d.\n", maxDepth);
    return false;
}

int main() {
    srand(time(NULL));

    // Simulasi data kondisi hutan dan posisi Alex
    Graph g;
    int numVertices = rand() % MAX_VERTICES + 1; // Jumlah simpul hutan acak antara 1 dan MAX_VERTICES
    initializeGraph(&g, numVertices);

    // Pilih posisi awal Alex secara acak
    int src = rand() % numVertices;

    // Pilih posisi jejak terakhir Alex secara acak
    int dest = rand() % numVertices;

    // Misalkan batas pencarian maksimum adalah 5 langkah
    int maxDepth = rand() % numVertices + 1; // batas maksimum acak antara 1 dan numVertices

    // Tambahkan beberapa edge secara acak untuk simulasi
    int numEdges = rand() % (numVertices * (numVertices - 1) / 2) + 1;
    for (int i = 0; i < numEdges; ++i) {
        int randomSrc = rand() % numVertices;
        int randomDest = rand() % numVertices;
        addEdge(&g, randomSrc, randomDest);
    }

    printf("Informasi pencarian:\n");
    printf("Posisi awal Alex: %d\n", src);
    printf("Posisi jejak terakhir Alex: %d\n", dest);
    printf("Batas pencarian maksimum: %d\n", maxDepth);

    // Pemilihan metode pencarian oleh pengguna
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

    return 0;
}
