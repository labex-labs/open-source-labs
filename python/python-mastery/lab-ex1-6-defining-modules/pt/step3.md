# Criando Seu Próprio Módulo

Agora que você entende como usar módulos existentes, é hora de criar um novo módulo do zero. Um módulo em Python é um arquivo que contém definições e declarações Python. Ele permite que você organize seu código em pedaços reutilizáveis ​​e gerenciáveis. Ao criar seu próprio módulo, você pode agrupar funções e variáveis ​​relacionadas, tornando seu código mais modular e fácil de manter.

## Criando um Módulo de Relatório

Vamos criar um módulo simples para gerar relatórios de ações. Este módulo terá funções para ler um arquivo de portfólio e imprimir um relatório formatado das ações no portfólio.

1. Primeiro, precisamos criar um novo arquivo chamado `report.py`. Para fazer isso, usaremos a linha de comando. Navegue até o diretório `project` em seu diretório home e crie o arquivo usando o comando `touch`.

```bash
cd ~/project
touch report.py
```

2. Agora, abra o arquivo `report.py` em seu editor de texto preferido e adicione o seguinte código. Este código define duas funções e um bloco principal.

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

A função `read_portfolio` lê um arquivo contendo informações sobre ações e retorna uma lista de dicionários, onde cada dicionário representa uma ação com as chaves `name`, `shares` e `price`. A função `print_report` recebe um portfólio (uma lista de dicionários de ações) e imprime um relatório formatado mostrando o nome da ação, o número de ações, o preço e o valor total. O bloco principal no final é executado quando o arquivo é executado diretamente. Ele lê o arquivo do portfólio e imprime o relatório.

3. Depois de adicionar o código, salve e saia do editor.

## Testando Seu Módulo

Vamos testar nosso novo módulo para garantir que ele funcione conforme o esperado.

1. Primeiro, executaremos o script diretamente da linha de comando. Isso executará o bloco principal no arquivo `report.py`.

```bash
python3 report.py
```

Você deve ver um relatório formatado mostrando as ações do portfólio e seus valores. Este relatório inclui o nome da ação, o número de ações, o preço e o valor total, bem como o valor total de todo o portfólio.

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. Em seguida, usaremos o módulo do interpretador Python. Inicie o interpretador Python executando o comando `python3` no terminal.

```bash
python3
```

Depois que o interpretador estiver em execução, podemos importar o módulo `report` e usar suas funções.

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

A declaração `import report` torna as funções e variáveis ​​definidas no arquivo `report.py` disponíveis na sessão Python atual. Em seguida, usamos a função `read_portfolio` para ler o arquivo do portfólio e armazenar o resultado na variável `portfolio`. A declaração `len(portfolio)` retorna o número de ações no portfólio, e `portfolio[0]` retorna a primeira ação no portfólio.

Você deve ver a seguinte saída:

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. Agora, vamos usar o módulo importado para calcular o custo total do portfólio nós mesmos. Iteraremos sobre as ações no portfólio e somaremos o valor total de cada ação.

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

A saída deve ser `44671.15`, que é o mesmo que o valor total impresso pela função `print_report`.

4. Finalmente, vamos criar um relatório personalizado para um tipo de ação específico. Filtraremos o portfólio para incluir apenas as ações da IBM e, em seguida, usaremos a função `print_report` para imprimir um relatório para essas ações.

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

Isso deve imprimir um relatório mostrando apenas as ações da IBM e seus valores.

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. Quando terminar de testar, saia do interpretador Python executando o comando `exit()`.

```python
exit()
```

Você agora criou e usou com sucesso seu próprio módulo Python, combinando funções e um bloco principal que só é executado quando o arquivo é executado diretamente. Essa abordagem modular de programação permite que você reutilize código e torne seus projetos mais organizados e fáceis de manter.
