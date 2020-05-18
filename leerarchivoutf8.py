# codigo para abrir un archivo usando utf8


archivo = open("./archivos/carreras.txt","r",encoding='utf8')

print(archivo.read())

archivo.close()