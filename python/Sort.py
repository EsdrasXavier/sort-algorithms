
def bubble_sort(arr):
  arr_len = len(arr)
  for i in range(arr_len):
    for j in range(i + 1, arr_len):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

  return arr


def recursive_bubble_sort(arr):
  arr_len = len(arr)
  for i in range(arr_len):
    try:
      if arr[i + 1] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
        recursive_bubble_sort(arr)
    except IndexError:
      pass

  return arr


def selection_sort(arr):
  arr_len = len(arr)

  for i in range(arr_len):
    _id = i # Minimun id to swap later
    for j in range(i + 1, arr_len):
      if arr[_id] > arr[j]: _id = j

    arr[i], arr[_id] = arr[_id], arr[i]

  return arr


def insertion_sort(arr):
  arr_len = len(arr)

  for i in range(1, arr_len):
    j, value = i, arr[i]

    while j > 0 and value < arr[j - 1]:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = value

  return arr