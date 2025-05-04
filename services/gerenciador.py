from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.produto import Produto
from views.exibidor import ExibidorProduto


class GerenciadorProduto:
    
    def __init__(self, exibidor: ExibidorProduto):
        self.exibidor = exibidor
    
    def processar_produto(self, produto: "Produto") -> None:
        self.exibidor.exibir(produto)
    
    def processar_varios_produtos(self, produtos: list["Produto"]) -> None:
        for produto in produtos:
            self.processar_produto(produto)
            print("-" * 40)