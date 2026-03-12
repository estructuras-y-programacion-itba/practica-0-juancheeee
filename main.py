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
    dados = tirar_dados(5)
    print("Dados:", dados)
    
    
# No cambiar a partir de aqui
if __name__ == "__main__":
    main()