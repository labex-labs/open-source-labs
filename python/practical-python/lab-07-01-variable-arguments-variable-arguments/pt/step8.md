# Exercício 7.4: Passagem de argumentos (Argument pass-through)

A função `fileparse.parse_csv()` tem algumas opções para alterar o delimitador de arquivo e para relatórios de erros. Talvez você queira expor essas opções para a função `read_portfolio()` acima. Faça esta alteração:

    def read_portfolio(filename, **opts):
        '''
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

Depois de fazer a alteração, tente ler um arquivo com alguns erros:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
```

Agora, tente silenciar os erros:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
