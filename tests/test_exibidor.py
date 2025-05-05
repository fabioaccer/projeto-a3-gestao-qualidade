import unittest
from io import StringIO
from unittest.mock import patch
from models.produto import Produto
from services.desconto import DescontoSempre
from views.exibidor import ExibidorConsole, ExibidorDetalhado, ExibidorJSON, ExibidorProduto


class TestExibidor(unittest.TestCase):
    
    def setUp(self):
        self.produto_com_desconto = Produto("Teste", 100.0, 0.1, DescontoSempre())
        self.produto_sem_desconto = Produto("Teste", 50.0, 0.0, DescontoSempre())
    
    def test_exibidor_console_com_desconto(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exibidor = ExibidorConsole()
            exibidor.exibir(self.produto_com_desconto)
            output = fake_out.getvalue().strip()
            
            self.assertIn("Produto: Teste", output)
            self.assertIn("Preço original: R$ 100.00", output)
            self.assertIn("Preço com desconto: R$ 90.00", output)
    
    def test_exibidor_console_sem_desconto(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exibidor = ExibidorConsole()
            exibidor.exibir(self.produto_sem_desconto)
            output = fake_out.getvalue().strip()
            
            self.assertIn("Produto: Teste", output)
            self.assertIn("Preço original: R$ 50.00", output)
            self.assertIn("Desconto não aplicável", output)
    
    def test_exibidor_detalhado_com_desconto(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exibidor = ExibidorDetalhado()
            exibidor.exibir(self.produto_com_desconto)
            output = fake_out.getvalue().strip()
            
            self.assertIn("PRODUTO: TESTE", output)
            self.assertIn("Preço original: R$ 100.00", output)
            self.assertIn("Desconto configurado: 10.0%", output)
            self.assertIn("Preço com desconto: R$ 90.00", output)
            self.assertIn("Economia: R$ 10.00", output)
    
    def test_exibidor_detalhado_sem_desconto(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exibidor = ExibidorDetalhado()
            exibidor.exibir(self.produto_sem_desconto)
            output = fake_out.getvalue().strip()
            
            self.assertIn("PRODUTO: TESTE", output)
            self.assertIn("Preço original: R$ 50.00", output)
            self.assertIn("Desconto configurado: 0.0%", output)
            self.assertIn("Desconto não aplicável para este produto", output)
    
    def test_exibidor_json_com_desconto(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exibidor = ExibidorJSON()
            exibidor.exibir(self.produto_com_desconto)
            output = fake_out.getvalue().strip()
            
            self.assertIn('"nome": "Teste"', output)
            self.assertIn('"preco_original": 100.0', output)
            self.assertIn('"desconto_percentual": 10.0', output)
            self.assertIn('"preco_com_desconto": 90.0', output)
            self.assertIn('"desconto_aplicado": true', output)
    
    def test_exibidor_json_sem_desconto(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exibidor = ExibidorJSON()
            exibidor.exibir(self.produto_sem_desconto)
            output = fake_out.getvalue().strip()
            
            self.assertIn('"nome": "Teste"', output)
            self.assertIn('"preco_original": 50.0', output)
            self.assertIn('"desconto_percentual": 0.0', output)
            self.assertIn('"preco_com_desconto": 50.0', output)
            self.assertIn('"desconto_aplicado": false', output)

    def test_exibidor_produto_abstrato(self):
        with self.assertRaises(TypeError):
            ExibidorProduto()


if __name__ == '__main__':
    unittest.main() 