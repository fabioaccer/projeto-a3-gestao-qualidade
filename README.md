# Projeto A3 - Gestão e Qualidade

Este projeto implementa um sistema de gestão de qualidade com funcionalidades para produtos, descontos e exibição de informações.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas listadas em `requirements.txt` ou `pyproject.toml`

## Instalação

### Windows

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd projeto-a3-gestao-qualidade
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Mac

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd projeto-a3-gestao-qualidade
   ```

2. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

### Windows

Para executar o programa principal:
```bash
python main.py
```

Para executar os testes:
```bash
python -m unittest discover tests
```

Para verificar a cobertura de testes:
```bash
coverage run -m unittest discover tests
coverage report
```

### Mac

Para executar o programa principal:
```bash
python3 main.py
```

Para executar os testes:
```bash
python3 -m unittest discover tests
```

Para verificar a cobertura de testes:
```bash
coverage run -m unittest discover tests
coverage report
```

## Estrutura do Projeto

- `models/`: Classes de modelo (ex: Produto)
- `services/`: Serviços (ex: GerenciadorProduto, CalculadorDesconto)
- `views/`: Exibidores (ex: ExibidorConsole, ExibidorDetalhado, ExibidorJSON)
- `tests/`: Testes unitários

## Responsáveis

- Fabio Ferreira de Lima Martins - RA: 82329580
- Flávio Henrique da Silva Junior - RA: 12624213181
- Jeziel Souza do Carmo - RA: 324137502
- Juarez De Matos Saliba - RA: 324118073
- Kauan Henrique Siviero - RA: 12524134992
- Sami de Santana Pereira - RA: 12722217872