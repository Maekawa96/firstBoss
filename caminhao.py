'''Altura aproximada?
Comprimento aproximado?
Largura aproximada?
Veiculo é Toco, Trucado ou Traçado?
Veiculo é cavalo mecânico ou Conjunto único?
Tipo de carroceria ?'''

from main import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    #Sobrescrita do método __str__()
    def __str__(self):

        retorno = super().__str__()
        return f'''{retorno}
 - Capacidade: {self.__capacidade}'''
    