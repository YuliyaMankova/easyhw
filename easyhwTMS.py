import random

def pin(col, nach, kon):
  for i in range(0, col):
    yield random.randint(nach, kon)

a = pin(5, 1000, 9999)
#next(a)
for i in a:
  print(i)