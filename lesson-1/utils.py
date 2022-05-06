def Q(n):
  n = str(bin(n)[2:])
  i = len(n) - 1
  j = 0
  while n[i] == '0':
    j += 1
    i -= 1
  return j
