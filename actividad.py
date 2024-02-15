import Crypto.Util.number
import hashlib
#DECODIFICAR LA FIRMA DE ALICIA CON BERNARDO

bits = 1024

# Obtener llave de Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

# Llave publica
nA = pA * qA

#Calcular indicador Euler Phi
phiA = (pA - 1) * (qA - 1)
#Euler
e = 65537

# Llave privada
dA = Crypto.Util.number.inverse(e, phiA)
print("Llave privada: ", dA, "\n")

#Mensaje en hash
#msg = 'Hola tonotos'
#hash = int.from_bytes(msg.encode('utf-8'), byteorder='big')
hash = hashlib.new('sha256')
hash.update(b"Hola tonotos")
hash_value = hash.hexdigest()
hash_int = int(hash_value, 16)

#Firma
firma = pow(hash_int, dA, nA)
print("Firma: ", firma, "\n")

#Verificar que sea el hash de Alice
verificar = pow(firma, e, nA)

print("Verificar: ", verificar, "\n")
if(verificar == hash_int):
    print("Si es el hash de Alice")




