import os

pasta_raiz = r"C:\Users\italo\OneDrive\Documentos"
lista = os.listdir(pasta_raiz)

for pastas in lista:
    print(pastas)