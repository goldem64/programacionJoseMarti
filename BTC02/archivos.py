file = open("archivo1.txt")

linea = file.readline()

while linea != "":
	print (linea)
	linea = file.readline()

print ("Hola")
print ("Mundo")


print ("Procesando archivo linea por linea con for")

file.close()

archivo = open ("archivo1.txt")
for linea in archivo:
	print (linea, end="")

archivo.close()

file = open("archivo1.txt")

lineas = file.readlines()

print ("Procesando todas las lineas del archivo")
print  (lineas)