from typing import Optional
from services.desconto import CalculadorDesconto

class Produto:
    
    def __init__(self, nome: str, preco: float, desconto: float = 0.0, 
                 calculador: Optional[CalculadorDesconto] = None):
        self._validar_dados(nome, preco, desconto)
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
        if calculador is not None:
            self.calculador = calculador
        else:
            from services.desconto import DescontoCondicional
            self.calculador = DescontoCondicional()
    
    def _validar_dados(self, nome: str, preco: float, desconto: float) -> None:
        if not nome or not nome.strip():
            raise ValueError("Nome do produto não pode estar vazio")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if not (0 <= desconto <= 1):
            raise ValueError("Desconto deve estar entre 0 e 1")
    
    def obter_preco_com_desconto(self) -> float:
        return self.calculador.calcular(self.preco, self.desconto)
    
    def aplicar_desconto(self, novo_desconto: float) -> None:
        if not (0 <= novo_desconto <= 1):
            raise ValueError("Desconto deve estar entre 0 e 1")
        self.desconto = novo_desconto