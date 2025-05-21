# Lendo uma Carteira de um Arquivo CSV

Nesta etapa, vamos criar uma função que lê dados de ações de um arquivo CSV e retorna uma lista de objetos `Stock`. Um objeto `Stock` representa uma participação acionária e, ao final desta etapa, você poderá ler uma carteira de ações de um arquivo CSV.

## Entendendo Arquivos CSV

CSV, que significa Valores Separados por Vírgula (Comma-Separated Values), é um formato muito comum para armazenar dados tabulares. Pense nisso como uma planilha simples. Cada linha em um arquivo CSV representa uma linha de dados, e as colunas dentro dessa linha são separadas por vírgulas. Normalmente, a primeira linha de um arquivo CSV contém cabeçalhos. Esses cabeçalhos descrevem que tipo de dados está em cada coluna. Por exemplo, em um CSV de carteira de ações, os cabeçalhos podem ser "Nome", "Ações" e "Preço".

## Instruções de Implementação

1. Primeiro, abra o arquivo `stock.py` no seu editor de código. Se já estiver aberto, ótimo! Caso contrário, encontre-o e abra-o. É aqui que adicionaremos nossa nova função.

2. Depois que o arquivo `stock.py` estiver aberto, procure o comentário `# TODO: Add read_portfolio(filename) function here`. Este comentário é um espaço reservado que nos diz onde colocar nossa nova função.

3. Abaixo desse comentário, adicione a seguinte função. Esta função é chamada `read_portfolio` e recebe um nome de arquivo como argumento. O objetivo desta função é ler o arquivo CSV, extrair os dados das ações e criar uma lista de objetos `Stock`.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

Vamos detalhar o que essa função faz. Primeiro, ela cria uma lista vazia chamada `portfolio`. Em seguida, ela abre o arquivo CSV no modo de leitura. A instrução `next(f)` pula a primeira linha, que é a linha do cabeçalho. Depois disso, ela percorre cada linha do arquivo. Para cada linha, ela divide a linha em uma lista de valores, extrai o nome, o número de ações e o preço, cria um objeto `Stock` e o adiciona à lista `portfolio`. Finalmente, ela retorna a lista `portfolio`.

4. Depois de adicionar a função, salve o arquivo `stock.py`. Você pode fazer isso pressionando `Ctrl+S` no seu teclado ou selecionando "File > Save" no menu do seu editor de código. Salvar o arquivo garante que suas alterações sejam preservadas.

5. Agora, precisamos testar nossa função `read_portfolio`. Crie um novo script Python chamado `test_portfolio.py`. Este script importará a função `read_portfolio` do arquivo `stock.py`, lerá a carteira de um arquivo CSV e imprimirá informações sobre cada ação na carteira.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

Neste script, primeiro importamos a função `read_portfolio`. Em seguida, chamamos a função com o nome do arquivo `portfolio.csv` para obter a lista de objetos `Stock`. Depois disso, percorremos a lista e imprimimos informações sobre cada ação. Finalmente, imprimimos o número total de ações na carteira.

6. Para executar o script de teste, abra seu terminal ou prompt de comando, navegue até o diretório onde o arquivo `test_portfolio.py` está localizado e execute o seguinte comando:

```bash
python3 test_portfolio.py
```

Se tudo estiver funcionando corretamente, você deverá ver uma saída que lista todas as ações do arquivo `portfolio.csv`, juntamente com seus nomes, número de ações e preços. Você também deverá ver o número total de ações na carteira.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

Esta saída confirma que sua função `read_portfolio` está lendo corretamente o arquivo CSV e criando objetos `Stock` a partir de seus dados.
