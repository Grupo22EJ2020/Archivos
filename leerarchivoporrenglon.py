#codigo para leer un archivo renglon X renglon
archivo = open('./archivos/carreras.txt',"r",encoding='utf8')
for renglon in archivo:
    print(f"No. Caracteres: {len(renglon)}: Renglon: {renglon}")
archivo.close()