# Doc Strings (Strings de Documentação)

É uma boa prática incluir documentação na forma de uma doc-string (string de documentação). Doc-strings são strings escritas imediatamente após o nome da função. Elas alimentam `help()`, IDEs e outras ferramentas.

```python
def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Uma boa prática para doc strings é escrever um resumo curto de uma frase sobre o que a função faz. Se mais informações forem necessárias, inclua um exemplo curto de uso, juntamente com uma descrição mais detalhada dos argumentos.
