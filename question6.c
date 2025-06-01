// MBANGA TSHIBANDA ---PREPOLYTECHNIQUE UNIKIN---
// TRAVAIL PRATIQUE D'INFORMATIQUE N°1
// QUESTION 6

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define CACHE_SIZE 8 * 1024          // 8 KB (cache)
#define RAM_SIZE 50 * 1024 * 1024    // 50 MB (RAM)
#define NB_ITER 100

void test_access_time(int *array, size_t size, const char *label) {
    LARGE_INTEGER start, end, freq;
    volatile int sum = 0;

    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&start);

    for (int j = 0; j < NB_ITER; j++) {
        for (size_t i = 0; i < size; i += 64) {
            sum += array[i];
        }
    }

    QueryPerformanceCounter(&end);

    double elapsed = (double)(end.QuadPart - start.QuadPart) / freq.QuadPart;
    printf("%s : %.4f secondes\n", label, elapsed);
}

int main() {
    int *cache_array = (int*)malloc(CACHE_SIZE * sizeof(int));
    int *ram_array = (int*)malloc(RAM_SIZE * sizeof(int));

    if (!cache_array || !ram_array) {
        printf("Erreur d'allocation mémoire.\n");
        return 1;
    }

    for (size_t i = 0; i < CACHE_SIZE; i++) cache_array[i] = i;
    for (size_t i = 0; i < RAM_SIZE; i++) ram_array[i] = i;

    test_access_time(cache_array, CACHE_SIZE, "Accès mémoire (cache)");
    test_access_time(ram_array, RAM_SIZE, "Accès mémoire (RAM)");

    free(cache_array);
    free(ram_array);
    return 0;
}
