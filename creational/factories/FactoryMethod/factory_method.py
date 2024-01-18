"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod
import re


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: ...


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Cliente solicitando Carro de luxo')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Cliente solicitando Carro popular')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Cliente solicitando Moto popular')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Cliente solicitando Moto de luxo')


class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: ...

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


class ZonaNorteFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'


class ZonaSulFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'motoluxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    from random import choice
    carros_disponiveis_zn = ['luxo', 'popular']
    carros_disponiveis_zs = ['luxo', 'popular', 'moto', 'motoluxo']

    print('ZONA NORTE')

    for i in range(10):
        carrozn = ZonaNorteFactory(choice(carros_disponiveis_zn))
        carrozn.buscar_cliente()

    print()

    print('ZONA SUL')

    for i in range(10):
        carrozs = ZonaSulFactory(choice(carros_disponiveis_zs))
        carrozs.buscar_cliente()
