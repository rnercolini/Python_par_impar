# Verifica se um número é par ou ímpar.
n = int(input('Digite um número qualquer: '))
m = n % 2
if m == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))
