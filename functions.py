from operator import index, xor
import string
import os

HEXADECIMAL_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
  'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

SNOW3G_byte = '10101001'
AES_byte = '00011011'

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Comprueba si un cadena es un número hexadecimal
def isHexadecimalDigit(hexa):
  for digit in hexa:
    if (digit in HEXADECIMAL_DIGITS == False):
      return False
  return True

# Convertir de hexadecimal a binario
def hexaToBin(hexa: string):
  result = ''
  for digit in hexa:
    if (isHexadecimalDigit(digit) == False):
      return None
    result += str(bin(int(digit, 16))[2:].zfill(4))
  return result

# Comprueba que una cadena sea un byte, esto es que sea una cadena
# de 1's y 0's con longitud 8
def isByte(byte: string):
  if (len(byte) != 8):
    return False
  else:
    for bit in byte:
      if (bit != '1' and bit != '0'):
        return False
    return True


# Devuelve una lista con los índices de aquellas posiciones que tengan
# valor 1 de un byte introducido por parámetro
def getByteIndexsWithValue1(byte: string):
  if (isByte(byte) == False):
    return None
  result = []
  it = len(byte)
  while it > 0:
    if (byte[it - 1] == '1'):
      result.append(len(byte) - it)
    it -= 1
  return result


# Realiza la operación XOR sobre 2 bytes
# Estos deben ser cadenas de 1's y 0's de longitud 8
def XORBytes(byte1, byte2):
  if (isByte(byte1) == False or isByte(byte2) == False):
    return None
  if (len(byte1) != len(byte2)):
    return None
  else:
    result = ''
    it = 0
    while (it < len(byte1)):
      if (byte1[it] == byte2[it]):
        result += '0'
      else:
        result += '1'
      it += 1
    return result

# Realiza el desplazamiento del algoritmo.
# El byte introducido debe expresarse como cadena de 8 bits
def shiftByte(byte, const):
  if (isByte(byte) == False):
    return None
  if (byte[0] == '0'):
    return byte[1:] + '0'
  else:
    return XORBytes(byte[1:] + '0', const)

# Multiplicación binaria de 2 bytes
# Los bits deben ser enteros de 8 bits
def binaryByteMultiplication(byte1, byte2, const):
  result = '00000000'
  iterableByte = byte1
  it = 0
  while (it <= max(getByteIndexsWithValue1(byte2))):
    if (it in getByteIndexsWithValue1(byte2)):
      result = XORBytes(result, iterableByte)
    iterableByte = shiftByte(iterableByte, const)
    it += 1
  return result

print(binaryByteMultiplication('01010111', '10000011', AES_byte))
