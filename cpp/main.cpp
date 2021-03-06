/**
 * Main file of sort algorithms in c++
 * To compile use: g++ main.cpp -o main
 * Or just type into terminal: make
*/

#include <iostream>
#include "Sort.hpp"

using namespace std;

#define ARRAY_LENGHT 10


int main(int argv, char *argc[]) {

  int arr[ARRAY_LENGHT] = {5, 2, 4, 9, 8, 3, 1, 7, 2, 6};

countingSort(arr, ARRAY_LENGHT);

  for (int i = 0; i < ARRAY_LENGHT; i++)
    cout << arr[i] << (i < ARRAY_LENGHT - 1 ? ", " : "");

  cout << endl;
  return 0;
}