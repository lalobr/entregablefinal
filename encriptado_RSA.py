import sys


def extract_info(flag):
    i = sys.argv.index(flag) + 1
    return sys.argv[i]


if '-pq' not in sys.argv:
    print ('debes ingresar un valor p y q')
    sys.exit(1)

if '--key' not in sys.argv:
    print ('debes ingresar la llave')
    sys.exit(1)

if '-m' not in sys.argv:
    print ('debes ingresar el mensaje')
    sys.exit(1)

pq = int(extract_info('-pq'))
llave = int(extract_info('--key'))
m = int(extract_info('-m'))

exp = m ** llave
mensaje_encriptado= exp % pq
print('tu mensaje encriptado o descencriptado es ' + str(mensaje_encriptado))