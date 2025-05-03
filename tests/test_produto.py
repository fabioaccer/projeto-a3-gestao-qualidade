import unittest
from models.produto import Produto
from services.desconto import DescontoCondicional, DescontoSempre


class TestProduto(unittest.TestCase):
    
    def test_produto_valido(self):
        produto = Produto("Teste", 100.0, 0.1)
        self.assertEqual(produto.nome, "Teste")
        self.assertEqual(produto.preco, 100.0)
        self.assertEqual(produto.desconto, 0.1)
    
    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            Produto("", 100.0, 0.1)
    
    def test_preco_negativo(self):
        with self.assertRaises(ValueError):
            Produto("Teste", -10.0, 0.1)
    
    def test_desconto_condicional(self):
        produto = Produto("Teste", 150.0, 0.1, DescontoCondicional())
        self.assertEqual(produto.obter_preco_com_desconto(), 135.0)
        
        produto_sem_desconto = Produto("Teste", 50.0, 0.1, DescontoCondicional())
        self.assertEqual(produto_sem_desconto.obter_preco_com_desconto(), 50.0)


if __name__ == "__main__":
    unittest.main()