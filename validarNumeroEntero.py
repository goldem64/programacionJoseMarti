def cuadrado():
    print ("Programa : Calcular cuadrado de un numero")
    espacios(3)
    while True:
        nombre = input ("Nombre : ")
        if not(validarCadena(nombre)):
            print ("Nombre no valido")
        else:
            break
    while True:
        numero = input("Numero : ")
        if not(validarNumero(numero)):
            print (numero + " " + "No es un numero")
            
        else:
            numero = int(numero)
            print ("Hola "+ nombre + " el cuadrado de " + str(numero) + " es : " + str(numero ** 2))
            break




def validarNumero(numero):
        
        if numero.isdigit():
            return True
        else:
            return False
def validarCadena(cadena):        
        if cadena.isalpha():
            return True
        else:
            return False
def espacios(n):
    if n ==1:
        print ("")
    elif n>1:
        for i in range(0,n):
            print ("")
    


cuadrado()
