# ----------------------------------------------------------------
# Práctica 5: Multiplicación en SNOW3G y AES
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 31/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from functions import *
import sys

# Constantes
SNOW3G_byte = '10101001'
AES_byte = '00011011'

# Main
cleanTerminal()

# Lectura de opciones
print("\n PRÁCTICA 5: MULTIPLICACIÓN EN SNOW 3G y AES\n")

byte1 = input("  Primer byte: ")
if (isHexadecimalDigit(byte1) == False or len(byte1) > 2):
  sys.exit('El byte introducido no es correcto...')
byte2 = input('  Segundo byte: ')
if (isHexadecimalDigit(byte2) == False or len(byte2) > 2):
  sys.exit('El byte introducido no es correcto...')
algoritmo = input('  Algoritmo (AES | SNOW3G): ')
if (algoritmo != 'AES' and algoritmo != 'SNOW3G'):
  sys.exit('El algoritmo introducido no es correcto...')
print()

# Parámetros de entrada
byte1 = hexaToBin(byte1)
byte2 = hexaToBin(byte2)
const = SNOW3G_byte
if (len(byte1) == 4):
  byte1 = '0000' + byte1
if (len(byte2) == 4):
  byte2 = '0000' + byte2
if (algoritmo == 'AES'):
  const = AES_byte

# Impresión por pantalla de los resultados
print(' > Primer byte: ' + byte1)
print(' > Segundo byte: ' + byte2)
print(' > Byte algoritmo: ' + const)
print(' > Multiplicación: ' + binaryByteMultiplication(byte1, byte2, const))