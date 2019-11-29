import re

path = "Prueba.txt"

try:
    archivo = open(path, 'r')
except:
    print ("El Archivo No Se Encuentra En Esta Carpeta")
    quit()

texto = ""

for linea in archivo:
    texto += linea

print (texto)
#Sentencia de asignacion
patronSENTENCIA = r"([A-Za-z]+ [=]+ ([0-9]||[a-z]\w+))"
resultSENTENCIA = re.findall(patronSENTENCIA,texto)

print ("\n", resultSENTENCIA)

print("\n")

patronOAB = r'([A-Za-z]+[=]+([0-9]+\.[0-9]|[a-z])+ [+|-|*|/]+ [0-9])'
resultOAB = re.findall(patronOAB,texto)

print ("\n", resultOAB)

print("\n")

patronEBB = r'([A-Za-z]+ ([>=|!=])+ [0-9])'
resultEBB= re.findall(patronEBB,texto)

print("\n", resultEBB)

print("\n")

patronENCABEZADO = r'([if]+ [a-z]+ [<|>|==]+ [0-9])|(for +[(]+[a-z]\w+ [a-z]+ [=]+ [0-9]+[;]+ [a-z]+ [<|>|=]+ [0-9]+[;])|([a-z]+[+]\W+[)])'
resultENCABEZADO = re.findall(patronENCABEZADO,texto)

print("\n", resultENCABEZADO)

print("\n")

patronFORMULAS = r'([a-z]+ [=]+ [a-z]+ [+|-|*|/]+ [(]+ [a-z]+ [+|-|*|/]+ [a-z]+[)])'
resultFORMULAS = re.findall(patronFORMULAS,texto)

print("\n", resultFORMULAS)

print("\n")