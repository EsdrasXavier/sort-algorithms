
def bubble_sort(arr):
  arr_len = len(arr)
  for i in range(arr_len):
    for j in range(i + 1, arr_len):
      if arr[i] > arr[j]:
        arr[i] ^= arr[j]
        arr[j] ^= arr[i]
        arr[i] ^= arr[j]

  return arr


def recursive_bubble_sort(arr):
  arr_len = len(arr)
  for i in range(arr_len):
    try:
      if arr[i + 1] < arr[i]:
        arr[i] ^= arr[j]
        arr[j] ^= arr[i]
        arr[i] ^= arr[j]
        recursive_bubble_sort(arr)
    except IndexError:
      pass

  return arr

