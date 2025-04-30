from abc import ABC, abstractmethod


class CalculadorDesconto(ABC):
    
    @abstractmethod
    def calcular(self, preco: float, desconto: float) -> float:
        pass


class DescontoCondicional(CalculadorDesconto):
    
    def __init__(self, valor_minimo: float = 100.0):
        self.valor_minimo = valor_minimo
    
    def calcular(self, preco: float, desconto: float) -> float:
        if preco > self.valor_minimo:
            return preco * (1 - desconto)
        return preco


class DescontoSempre(CalculadorDesconto):
    
    def calcular(self, preco: float, desconto: float) -> float:
        return preco * (1 - desconto)


class DescontoProgressivo(CalculadorDesconto):
    
    def calcular(self, preco: float, desconto: float) -> float:
        if preco > 500:
            return preco * (1 - desconto * 1.5)
        elif preco > 200:
            return preco * (1 - desconto * 1.2)
        elif preco > 100:
            return preco * (1 - desconto)
        return preco