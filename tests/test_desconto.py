import unittest
from services.desconto import DescontoCondicional, DescontoSempre, DescontoProgressivo, CalculadorDesconto


class TestDesconto(unittest.TestCase):
    
    def test_desconto_condicional_acima_minimo(self):
        calculador = DescontoCondicional(valor_minimo=100.0)
        preco = 150.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 135.0)  # 150 * (1 - 0.1)
    
    def test_desconto_condicional_abaixo_minimo(self):
        calculador = DescontoCondicional(valor_minimo=100.0)
        preco = 50.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 50.0)  # Sem desconto
    
    def test_desconto_condicional_valor_minimo_personalizado(self):
        calculador = DescontoCondicional(valor_minimo=200.0)
        preco = 250.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 225.0)  # 250 * (1 - 0.1)
    
    def test_desconto_sempre(self):
        calculador = DescontoSempre()
        preco = 100.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 90.0)  # 100 * (1 - 0.1)
    
    def test_desconto_progressivo_acima_500(self):
        calculador = DescontoProgressivo()
        preco = 600.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 510.0)  # 600 * (1 - 0.1 * 1.5)
    
    def test_desconto_progressivo_acima_200(self):
        calculador = DescontoProgressivo()
        preco = 300.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 264.0)  # 300 * (1 - 0.1 * 1.2)
    
    def test_desconto_progressivo_acima_100(self):
        calculador = DescontoProgressivo()
        preco = 150.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 135.0)  # 150 * (1 - 0.1)
    
    def test_desconto_progressivo_abaixo_100(self):
        calculador = DescontoProgressivo()
        preco = 50.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 50.0)  # Sem desconto

    def test_desconto_progressivo_igual_100(self):
        calculador = DescontoProgressivo()
        preco = 100.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 100.0)  # Sem desconto

    def test_desconto_condicional_igual_valor_minimo(self):
        calculador = DescontoCondicional(valor_minimo=100.0)
        preco = 100.0
        desconto = 0.1
        resultado = calculador.calcular(preco, desconto)
        self.assertEqual(resultado, 100.0)  # Sem desconto

    def test_calculador_desconto_abstrato(self):
        with self.assertRaises(TypeError):
            CalculadorDesconto()


if __name__ == '__main__':
    unittest.main() 