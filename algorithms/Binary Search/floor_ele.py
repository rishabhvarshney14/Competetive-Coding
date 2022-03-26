def floor_ele(arr, ele):
  start = 0
  end = len(arr) - 1
  result = -1
  
  while not start > end:
    mid = start + (end - start) // 2
    if arr[mid] == ele:
      return mid
    elif ele > arr[mid]:
      result = mid
      start = mid + 1
    else:
      end = mid - 1
          
  return result