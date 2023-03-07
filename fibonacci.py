r = 0
a = 1
b = 0
c = 0
i = 0
fibo = []

while r != 30:
  b = a + c
  c = a + b
  a = b + c
  fibo.insert(i, b)
  fibo.insert(i, c)
  fibo.insert(i, a)
  i += 1
  r += 1
numero = int(input("Informe o número que você deseja consultar: "))
if numero in fibo:
  print("O número {} pertence a sequência de fibonacci".format(numero))
else:
  print("O número {} não pertence a sequência de fibonacci".format(numero))


