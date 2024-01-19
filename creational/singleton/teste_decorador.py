def meu_decorador(func):
    def wrapper():
        print("Chamando a função", func.__name__)
        func()
    return wrapper


@meu_decorador
def meu_alvo():
    print("Eu sou um alvo!")


meu_alvo()
