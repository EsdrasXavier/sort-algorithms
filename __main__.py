from Sort import bubble_sort, recursive_bubble_sort

def main():
  arr = [5, 8, 6, 2, 78, 1, 2, 7, 56, 75]
  print("Bubble sort: {}".format(bubble_sort(arr)))
  print("Bubble sort: {}".format(recursive_bubble_sort(arr)))

if __name__ == '__main__':
  main()