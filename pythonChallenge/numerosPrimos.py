"""
Este codigo es para obtener todos los numeros primos hasta el numero que el usuario ingrese

La ruta donde se guarda el archivo .txt en el entorno de Cloud9 es: /home/ec2-user/numerosPrimos.txt

El codigo funciona en dos partes, en base a el numero que nos otorga el usuario, desde 1 hasta "numero" 
obtenemos todos los divisores de todos los numeros, despues con otra funcion en un ciclo "for" evaluamos todos los numeros
y sus divisores con que deban tener como divisores solo la unidad y el numero en si mismo [ 1, "numero"].
De cumplirse esta condicion es un numero primo y se agrega a la lista.

"""
def divisoresNumero(numero): #Obtenemos los divisores de cada numero
    lista = []
    for i in range(1, numero + 1):
        if numero%i == 0:
            lista.append(i)
    return lista

def numeroPrimo(numero): #Evaluamos los divisores con una igualdad de que sus divisores deben ser [ 1 , "numero"]
    numPrimos = ""
    for i in range(1, numero+1):
        divisores = divisoresNumero(i)
        if divisores == [1,i]:#Si se cumple la condicion es un numero primo y se agrega a la lista y se imprime en el documento .txt
            numPrimos += f'{i}  '
    with open('/home/ec2-user/numerosPrimos.txt','w',) as archivo:
        archivo.write(numPrimos)
    return  numPrimos


print('Ingrese hasta que numero desea conocer los numeros primos:')
numero = int(input( ))
print('Los numero primos son:')
print(f'{numeroPrimo(numero)}')
