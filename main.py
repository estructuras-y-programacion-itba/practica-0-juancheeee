import random

# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"


def tirar_dados(cantidad):
    dados = []
    
    for i in range(cantidad):
        dados.append(random.randint(1,6))
    
    return dados


def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()