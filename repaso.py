from metodos import insertar_numeros

lista_de_numeros = []

for i in range(3):
    numero = input("Introduce un número: ")
    insertar_numeros(lista_de_numeros, numero)
print(f"Los números son: {lista_de_numeros}")