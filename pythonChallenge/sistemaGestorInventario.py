"""

Este es un sistema gestor de inventario, lo separe por funciones, agregar, actualiza, eliminar, buscar producto y generar un informe
del inventario. 
La ruta donde se guarda el archivo .txt en el entorno de Cloud9 es: /home/ec2-user/informeInventario.txt

"""
import json

inventarioCelulares = { 
                        "Samsung":{
                            "galaxy z"  : 27000,
                            "galaxy s"  : 19000,
                            "galaxy a"  : 16000,
                            "galaxy tab": 13000
                                    },
                        "Huawei":{
                            "nova": 13000,
                            "p40"   : 18000,
                            "mate": 24000
                                    },
                        "Apple":{
                            "iphone 15"  : 35000,
                            "iphone 14"  : 26000,
                            "iphone 13"  : 18000,
                            "iphone X"   : 12000
                                    }
                        }

def agregarProducto():
    marcas = list(inventarioCelulares.keys())
    print(f'''Las marcas de telefonos que manejamos son las siguientes:\n {marcas}
¿De que marca desea agregar un nuevo producto?
1 - Samsung
2 - Huawei
3 - Apple
          ''')
    eleccion = input()
    modelo = input(f'''Por favor ingrese el modelo del celular: ''')
    precio = input(f'''Por favor ingrese el precio del celular: ''')
    try:
        if eleccion == '1':
            inventarioCelulares["Samsung"] [modelo] = precio
        elif eleccion == '2':
            inventarioCelulares["Huawei"] [modelo] = precio
        elif eleccion == '3':
            inventarioCelulares["Apple"] [modelo] = precio
        else:
            print("La marca solicitada no se maneja en nuestros servicios\n")
    except ValueError:
        print("¡Error! El precio debe ser un número entero.")

def actualizarProducto():
    print(f'''Nuestro inventario actual es el siguiente:''' )
    for marca, modelos in inventarioCelulares.items():
        print(f"\nMarca: {marca}")
        for modelo, precio in modelos.items():
            print(f"  - Modelo: {modelo}, Precio: {precio} pesos")
            
    print(f'''\n¿De cual modelo deseas actualizar su precio?
(Por favor ingresa el nombre del modelo como se muestran arriba, con mayusculas y miusculas)''')
    marcaCelular  = input('Por favor ingrese la marca: ')
    modeloCelular = input('Por favor ingresa el nombre del modelo: ')
    try:
        precioCelular = int(input('Por favor ingresa el precio del modelo: '))
        inventarioCelulares[marcaCelular][modeloCelular] = precioCelular
    except ValueError:
        print("¡Error! El precio debe ser un número entero.")
    
    print(f'El inventario actualizado quedaria de la siguiente manera:' )
    for marca, modelos in inventarioCelulares.items():
        print(f"\nMarca: {marca}")
        for modelo, precio in modelos.items():
            print(f"  - Modelo: {modelo}, Precio: {precio} pesos")

def eliminarProducto():
    print('El inventario actual es el sguiente:')
    for marca, modelos in inventarioCelulares.items():
        print(f'\n Marca: {marca}')
        for modelo, precio in modelos.items():
            print(f'\n Modelo: {modelo} - Precio: {precio}')
    print(f'''\nPara eliminar del inventario un producto, por favor ingrese los siguientes datos 
(Escribir como se muestra arriba, con mayusculas y minusculas)
          ''')
    marca = input('Marca: ')
    modelo= input('modelo: ')
    inventarioCelulares.pop([marca] [modelo], 'Este producto no se encuentra dentro del inventario.')

def buscarProducto():
    print(f'Para realizar una busqueda del modelo especifico, por favor ingrese una parte del nombre del equipo: ')
    cadena = input()
    coincidencias = []
    for marca, modelos in inventarioCelulares.items():
        for modelo, precio in modelos.items():
            if cadena in modelo:
                coincidencias.append((marca, modelo, precio))
    print('Los modelos encontrado dentro del inventario son:')
    for coincidencia in coincidencias:
        print(f'{coincidencia}\n')        

def generarInforme():
    print(f'¿Desea generar un informe del inventario actual?')
    inventario = input('1 Si \n2 No\n')
    if inventario == '1':
        with open('/home/ec2-user/informeInventario.txt','w',) as archivo:
            json.dump(inventarioCelulares, archivo)
            print('Informe del inventario generado con éxito, en la siguiente ruta: \n/home/ec2-user/informeInventario.txt.')
    elif inventario == '2':
        print('No se generará un informe.')
    else:
        print('Opción no válida. Por favor ingrese 1 para generar un informe o 2 para cancelar.')
    
def sistemaGestor():
    while True:
        print(f'''  
                     ##               ####                       ###                 
   ##                ##               #######
  #####    ####      ##      ####      #       ####    #####     ###      ####     ####
   ##     ##  ##     ##     ##  ##   #####    ##  ##   ##  ##     ##     ##  ##       ##
   ##     ######     ##     ######    ##      ##  ##   ##  ##     ##     ##        #####
   ## ##  ##         ##     ##        ##      ##  ##   ##  ##     ##     ##  ##   ##  ##
    ###    #####    ####     #####   ####      ####    ##  ##    ####     ####     #####

                                    Hola, buen día
                Bienvenido al sistema gestor de inventario de la telefonica
                ¿Que le gustaria realizar el dia de hoy?
                (1) Agregar un producto
                (2) Actualizar un producto
                (3) Eliminar un producto
                (4) Buscar un producto
                (5) Generar un informe del inventario actual
                (6) Salir''')
        try:
            accion = input()
            if accion == '1':
                agregarProducto()
            elif accion == '2':
                actualizarProducto()
            elif accion == '3':
                eliminarProducto()
            elif accion == '4':
                buscarProducto()
            elif accion == '5':
                generarInforme()
            elif accion == '6':
                break
            else:
                print('Por favor elija una de las opciones mencionadas arriba.')
        except ValueError:
            print('Por favor ingrese un número.')

sistemaGestor()