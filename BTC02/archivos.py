# con la funcion 'open' podemos abrir un archivo, no hay que olvidar indicar la extension del archivo
file = open("archivo1.txt")
# el metodo readline() permite almacenar una linea del archivo que estamos abriendo
linea = file.readline()

# este codigo nos permite procesar el archivo linea por linea e imprimirla
while linea != "":
	print (linea)
	linea = file.readline()
# cerramos el archivo
file.close()

# otra forma de procesar un archivo es utilizando un for e iterar el archivo, de esta forma iteramos el archivo por linea
print ("Procesando archivo linea por linea con for")



archivo = open ("archivo1.txt")
for linea in archivo:
	print (linea, end="")

archivo.close()

# una segunda forma de procesar el archivo es procesando la totalidad del archivo con la funcion  readlines

file = open("archivo1.txt")

lineas = file.readlines()

print ("Procesando todas las lineas del archivo")
print  (lineas)