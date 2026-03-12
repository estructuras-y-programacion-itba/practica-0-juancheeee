import random

# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"


def tirar_dados(cantidad):
    dados = []
    
    for i in range(cantidad):
        dados.append(random.randint(1,6))
    
    return dados

def contar_dados(dados):
    conteo = [0,0,0,0,0,0]

    for dado in dados:
        conteo[dado-1] += 1

    return conteo

def es_generala(conteo):
    for cantidad in conteo:
        if cantidad == 5:
            return True
    return False

def es_poker(conteo):
    for cantidad in conteo:
        if cantidad == 4:
            return True
    return False

def es_full(conteo):
    hay_tres = False
    hay_dos = False

    for cantidad in conteo:
        if cantidad == 3:
            hay_tres = True
        if cantidad == 2:
            hay_dos = True

    return hay_tres and hay_dos

def main():
    dados = tirar_dados(5)
    print("Dados:", dados)
    
    conteo = contar_dados(dados)
    print("Conteo:", conteo)
    
# No cambiar a partir de aqui
if __name__ == "__main__":
    main()