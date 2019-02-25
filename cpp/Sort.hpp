#include <iostream>

void swap_pos(int *a, int *b) {
  if (*a != *b) {
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
  }
}

void bubbleSort(int *arr, int len) {
  for (int i = 0; i < len; i++) {
    for (int j = i+1; j < len; j++) {
      if (arr[i] > arr[j]) swap_pos(&arr[i], &arr[j]);
    }
  }
}

void recursiveBubbleSort(int *arr, int len) {
  for (int i = 0; i < len; i++) {
    if (i + 1 >= len) break;
    if (arr[i + 1] < arr[i]) {
      swap_pos(&arr[i + 1], & arr[i]);
      recursiveBubbleSort(arr, len);
    }
  }
}