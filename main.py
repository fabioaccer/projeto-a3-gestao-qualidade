from models import Produto
from services import DescontoCondicional, DescontoProgressivo, GerenciadorProduto
from views import ExibidorConsole, ExibidorDetalhado, ExibidorJSON


def exemplo_basico():
    print("=== EXEMPLO BÁSICO ===")
    
    produto = Produto(
        nome="Tênis",
        preco=150.0,
        desconto=0.1
    )
    
    exibidor = ExibidorConsole()
    gerenciador = GerenciadorProduto(exibidor)
    gerenciador.processar_produto(produto)


def exemplo_avancado():
    print("\n=== EXEMPLO AVANÇADO ===")
    
    produtos = [
        Produto("Smartphone", 800.0, 0.15, DescontoProgressivo()),
        Produto("Livro", 50.0, 0.1, DescontoCondicional()),
        Produto("Notebook", 2500.0, 0.12, DescontoProgressivo()),
    ]
    
    exibidores = [
        ("Console Simples", ExibidorConsole()),
        ("Detalhado", ExibidorDetalhado()),
        ("JSON", ExibidorJSON()),
    ]
    
    for nome_exibidor, exibidor in exibidores:
        print(f"\n--- {nome_exibidor} ---")
        gerenciador = GerenciadorProduto(exibidor)
        gerenciador.processar_produto(produtos[0])


def main():
    """Função principal."""
    try:
        exemplo_basico()
        exemplo_avancado()
        
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()