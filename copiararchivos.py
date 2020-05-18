# codigo de ejemplo para copiar la informacion de un archivo
# y pasarla a uno nuevo

archivoorigen = open("./archivos/carreras.txt","r",encoding="utf8")
archivodestino = open("./archivos/copia.txt","w",encoding="utf8")

archivodestino.write(archivoorigen.read())

archivoorigen.close()
archivodestino.close()
