import Crypto.Util.number

# Establecer numero de bits
bits = 1024

# Obtener primos de Alice (llaves secretas)
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("pA:", pA, "\n")

qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("qA:", qA, "\n")

# Obtener los numeros de Bob
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("pB:", pB, "\n")

qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("qB:", qB, "\n")

# Obtener llaves publicas
nA = pA * qA
print("nB:", nA, "\n")
nB = pB * qB
print("nB:", nB, "\n")

# Calcular el indicador de Euler Phi
phiA = (pA - 1) * (qA - 1)
print("phiA:", phiA, "\n")

phiB = (pB - 1) * (qB - 1)
print("phiB:", phiB, "\n")

# Por razones mas eficientes usaremos el numero 4 de Fermat, 65537,
# debido a que es un primo largo y no es potencia de 2, y como forma
# parte de la llave pública no es necesario calcularlo

e = 65537

#Calcular la llave privada de Alice y Bob
dA = Crypto.Util.number.inverse(e, phiA)
print("dA:", dA, "\n")

dB = Crypto.Util.number.inverse(e, phiB)
print("dA:", dB, "\n")

#Ciframos el mensaje
msg='Hola tonotos'
print('Mensaje original: ', msg, "\n")
print("Longitud del mensaje en bytes: ", len(msg.encode('utf-8')))

#Convertir el mensaje a numero
m = int.from_bytes(msg.encode('utf-8'), byteorder='big')
print("Mensaje convertido en entero: ", m, "\n")

#Cifrar el mensaje
c = pow(m,e, nB)
print("Mensaje cifrado: ", c, "\n")

#Descifrar el mensaje
des = pow(c, dB, nB)
print("Mensaje descifrado:", des, "\n")

#Convertimos el mensaje de número a texto
msg_Final = int.to_bytes(des, len(msg), byteorder='big').decode('utf-8')
print("Mensaje final: ",msg_Final)