import functools

def sorting(arr, N):
  # instead using sorted() method
  arr = sorted(arr, key= functools.cmp_to_key(compare))
  print(arr)
def compare(item1, item2):
  if (item1 < item2):
    return -1
  else:
    return 1

if __name__ == "__main__":
  arr= [14, 1, 2, 12, 100, 1]
  N = len(arr)
  sorting(arr, N)
