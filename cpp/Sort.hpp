#include <iostream>

void swap(int *a, int *b) {
  if (*a != *b) {
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
  }
}

void bubbleSort(int *arr, int len) {
  for (int i = 0; i < len; i++) {
    for (int j = i+1; j < len; j++) {
      if (arr[i] > arr[j]) swap(&arr[i], &arr[j]);
    }
  }
}

void recursiveBubbleSort(int *arr, int len) {
  for (int i = 0; i < len; i++) {
    if (i + 1 >= len) break;
    if (arr[i + 1] < arr[i]) {
      swap(&arr[i + 1], &arr[i]);
      recursiveBubbleSort(arr, len);
    }
  }
}

void quickSort(int *arr, int low, int high) {

  if (low >= high) return ;

  int i = low - 1;
  int pivot = arr[high];
  for (int j = low; j < high; j++) {
    if (arr[j] <= pivot) {
      i++;
      swap(&arr[i], &arr[j]);
    }
  }
  i++;

  swap(&arr[i + 1], &arr[high]);
  quickSort(arr, low  , i - 1);
  quickSort(arr, i + 1, high);
}