n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
x = 0
y = 0
if n1 > 0:
    x += 1
    y = n1
if n2 > 0:
    x += 1
    y += n2
if n3 > 0:
    x += 1
    y += n3
if n4 > 0:
    x += 1
    y += n4
if n5 > 0:
    x += 1
    y += n5
if n6 > 0:
    x += 1
    y += n6

if x > 0:
  print('{:.0f} valores positivos'.format(x))
  media = y / x
  print('{:.1f}'.format(media))
