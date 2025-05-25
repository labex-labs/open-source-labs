# Exercício 4.5: Um Problema de Extensibilidade

Suponha que você quisesse modificar a função `print_report()` para suportar uma variedade de formatos de saída diferentes, como texto simples, HTML, CSV ou XML. Para fazer isso, você poderia tentar escrever uma função gigantesca que fizesse tudo. No entanto, fazê-lo provavelmente levaria a uma bagunça não sustentável. Em vez disso, esta é uma oportunidade perfeita para usar a herança.

Para começar, concentre-se nas etapas envolvidas na criação de uma tabela. No topo da tabela, há um conjunto de cabeçalhos de tabela. Depois disso, aparecem linhas de dados da tabela. Vamos pegar essas etapas e colocá-las em sua própria classe. Crie um arquivo chamado `tableformat.py` e defina a seguinte classe:

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
```

Esta classe não faz nada, mas serve como uma espécie de especificação de design para classes adicionais que serão definidas em breve. Uma classe como esta é, por vezes, chamada de "classe base abstrata".

Modifique a função `print_report()` para que ela aceite um objeto `TableFormatter` como entrada e invoque métodos nele para produzir a saída. Por exemplo, assim:

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

Como você adicionou um argumento a print_report(), você também precisará modificar a função `portfolio_report()`. Altere-a para que ela crie um `TableFormatter` assim:

```python
# report.py

import tableformat

...
def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

Execute este novo código:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... crashes ...
```

Ele deve travar imediatamente com uma exceção `NotImplementedError`. Isso não é muito emocionante, mas é exatamente o que esperávamos. Continue para a próxima parte.
