from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.produto import Produto


class ExibidorProduto(ABC):
    
    @abstractmethod
    def exibir(self, produto: 'Produto') -> None:
        pass


class ExibidorConsole(ExibidorProduto):
    
    def exibir(self, produto: 'Produto') -> None:
        print(f"Produto: {produto.nome}")
        print(f"Preço original: R$ {produto.preco:.2f}")
        
        preco_desconto = produto.obter_preco_com_desconto()
        if preco_desconto < produto.preco:
            print(f"Preço com desconto: R$ {preco_desconto:.2f}")
        else:
            print("Desconto não aplicável")


class ExibidorDetalhado(ExibidorProduto):
    
    def exibir(self, produto: 'Produto') -> None:
        print("=" * 50)
        print(f"PRODUTO: {produto.nome.upper()}")
        print("=" * 50)
        print(f"Preço original: R$ {produto.preco:.2f}")
        print(f"Desconto configurado: {produto.desconto * 100:.1f}%")
        
        preco_desconto = produto.obter_preco_com_desconto()
        if preco_desconto < produto.preco:
            economia = produto.preco - preco_desconto
            print(f"Preço com desconto: R$ {preco_desconto:.2f}")
            print(f"Economia: R$ {economia:.2f}")
        else:
            print("Desconto não aplicável para este produto")
        print("=" * 50)


class ExibidorJSON(ExibidorProduto):
    
    def exibir(self, produto: 'Produto') -> None:
        import json
        
        preco_desconto = produto.obter_preco_com_desconto()
        data = {
            "nome": produto.nome,
            "preco_original": produto.preco,
            "desconto_percentual": produto.desconto * 100,
            "preco_com_desconto": preco_desconto,
            "desconto_aplicado": preco_desconto < produto.preco
        }
        
        print(json.dumps(data, indent=2, ensure_ascii=False))