
def bubble_sort(arr):
  arr_len = len(arr)
  for i in range(arr_len):
    for j in range(i + 1, arr_len):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]


def recursive_bubble_sort(arr):
  arr_len = len(arr)
  for i in range(arr_len):
    try:
      if arr[i + 1] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
        recursive_bubble_sort(arr)
    except IndexError:
      pass


def selection_sort(arr):
  arr_len = len(arr)

  for i in range(arr_len):
    _id = i # Minimun id to swap later
    for j in range(i + 1, arr_len):
      if arr[_id] > arr[j]: _id = j

    arr[i], arr[_id] = arr[_id], arr[i]


def insertion_sort(arr):
  arr_len = len(arr)

  for i in range(1, arr_len):
    j, value = i, arr[i]

    while j > 0 and value < arr[j - 1]:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = value


def quick_sort(arr, *args, **kwargs):
  low = kwargs.get('low', 0)
  high = kwargs.get('high', len(arr) - 1)

  if low >= high: return

  i = low - 1
  pivot = arr[high]
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  pi = i + 1

  quick_sort(arr, low=low, high=pi-1)
  quick_sort(arr, low=pi + 1, high=high)


def merge_sort(arr):
  arr_len = len(arr)

  if arr_len < 2: return

  middle = arr_len / 2
  left = arr[:middle]
  right = arr[middle:]

  merge_sort(left)
  merge_sort(right)

  i = j = k = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1

  for l in range(i, len(left)):
    arr[k] = left[l]
    k += 1

  for l in range(j, len(right)):
    arr[k] = right[l]
    k += 1
