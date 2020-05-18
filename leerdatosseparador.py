# codigo para leer informacion de un archivo delimitado

archivo = open("./archivos/datos.txt","r")
for renglon in archivo:
    datosproducto = renglon.split('|')
    print(f'Clave: {datosproducto[0]} Nombre: {datosproducto[1]} Precio:{datosproducto[2]}')
archivo.close()