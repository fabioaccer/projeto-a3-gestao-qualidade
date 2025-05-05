import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from models.produto import Produto
from services.gerenciador import GerenciadorProduto
from views.exibidor import ExibidorProduto


class TestGerenciador(unittest.TestCase):
    
    def setUp(self):
        self.exibidor_mock = MagicMock(spec=ExibidorProduto)
        self.gerenciador = GerenciadorProduto(self.exibidor_mock)
        self.produto1 = Produto("Produto 1", 100.0)
        self.produto2 = Produto("Produto 2", 200.0)
    
    def test_processar_produto(self):
        self.gerenciador.processar_produto(self.produto1)
        self.exibidor_mock.exibir.assert_called_once_with(self.produto1)
    
    def test_processar_varios_produtos(self):
        produtos = [self.produto1, self.produto2]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.gerenciador.processar_varios_produtos(produtos)
            
            # Verifica se exibir foi chamado para cada produto
            self.assertEqual(self.exibidor_mock.exibir.call_count, 2)
            self.exibidor_mock.exibir.assert_any_call(self.produto1)
            self.exibidor_mock.exibir.assert_any_call(self.produto2)
            
            # Verifica se a linha separadora foi impressa
            output = fake_out.getvalue()
            self.assertEqual(output.count("-" * 40), 2)

    def test_construtor(self):
        self.assertIsInstance(self.gerenciador, GerenciadorProduto)

    def test_processar_varios_produtos_vazio(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.gerenciador.processar_varios_produtos([])
            output = fake_out.getvalue()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main() 