def isPallindrom(string: str, low: int, high: int) -> bool:
  while low < high:
    if string[low] != string[high]:
      return False
    low += 1
    high -= 1
  return True

def PalindromeCreator(string):
  low = 0
  high = len(string) - 1
  while low < high:
    if string[low] == string[high]:
      low += 1
      high -= 1
    else:
      if isPallindrom(string, low + 1, high):
        return string[low] 
      if isPallindrom(string, low, high - 1):
        return string[high] 
      return 'not possible'
  return 'not possible'

# keep this function call here 
print(PalindromeCreator(input()))