import math
import sys


def Nprimo(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
# >>python RSA_keygen.py -pq 2 3 -x 1
# >>sys.argv -> [RSA_keygen.py, -pq, 2, 3, -x, 1]

if '-pq' in sys.argv:
    flag_index = sys.argv.index('-pq')
    flag_index += 1
    p = int(sys.argv[flag_index])
    flag_index += 1
    q = int(sys.argv[flag_index])
else:
    p = 1009
    q = 2741

if not Nprimo(p) or not Nprimo(q):
    raise ValueError('p o q no son primos')

if '-x' in sys.argv:
    flag_index = sys.argv.index('-x')
    flag_index += 1
    x = int(sys.argv[flag_index])
else:
    x = 1

eq = (p - 1) * (q - 1) + 1

y = 1
xy = x*y

while xy != eq:
    x += 1
    y = eq // x
    xy = x*y


print ("llave pública, x: " + str(x))
print ("llave privada, y: " + str(y))
print ("módulo (pq): " + str(p*q))