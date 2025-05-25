# Exercício 4.7: Polimorfismo em Ação

Uma característica importante da programação orientada a objetos é que você pode conectar um objeto em um programa e ele funcionará sem ter que alterar nenhum dos códigos existentes. Por exemplo, se você escreveu um programa que esperava usar um objeto `TableFormatter`, ele funcionaria, independentemente do tipo de `TableFormatter` que você realmente fornecesse. Esse comportamento é, por vezes, referido como "polimorfismo".

Um problema potencial é descobrir como permitir que um usuário escolha o formatador que deseja. O uso direto dos nomes das classes, como `TextTableFormatter`, é frequentemente irritante. Assim, você pode considerar alguma abordagem simplificada. Talvez você incorpore uma instrução `if-` no código assim:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_report(report, formatter)
```

Neste código, o usuário especifica um nome simplificado como `'txt'` ou `'csv'` para escolher um formato. No entanto, colocar uma grande instrução `if`- na função `portfolio_report()` dessa forma é a melhor ideia? Pode ser melhor mover esse código para uma função de uso geral em outro lugar.

No arquivo `tableformat.py`, adicione uma função `create_formatter(name)` que permita a um usuário criar um formatador, dado um nome de saída como `'txt'`, `'csv'` ou `'html'`. Modifique `portfolio_report()` para que fique assim:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

Tente chamar a função com diferentes formatos para garantir que ela esteja funcionando.
