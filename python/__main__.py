from Sort import *

def main():
  arr = [99, 5, 8, 6, 2, 78, 12, 7, 56, 75, 1]
  # print("Bubble sort: {}".format(bubble_sort(arr)))
  # print("Recursive Bubble sort: {}".format(recursive_bubble_sort(arr)))
  # print("Selection sort: {}".format(selection_sort(arr)))
  counting_sort(arr)
  print("Insetion sort: {}".format(arr))

if __name__ == '__main__':
  main()
