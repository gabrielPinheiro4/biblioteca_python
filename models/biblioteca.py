from utils.funcoes import csv_arquivo_biblioteca


class Biblioteca:

    def __init__(self, nome, endereco, numero, quantidade_catalogo):
        self.__nome = nome
        self.__endereco = endereco
        self.__numero = numero
        self.__quantidade_catalogo = quantidade_catalogo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def quantidade_catalogo(self):
        return self.__quantidade_catalogo

    
# Instanciando o objeto com os dados do arquivo bibliotecas.csv
biblioteca = Biblioteca(
    csv_arquivo_biblioteca('Nome da Biblioteca'),
    csv_arquivo_biblioteca('Endereço'),
    csv_arquivo_biblioteca('Número'),
    csv_arquivo_biblioteca('Quantidade de Catálogos')
)