# Exercício 3.9: Capturando exceções

A função `parse_csv()` que você escreveu é usada para processar todo o conteúdo de um arquivo. No entanto, no mundo real, é possível que os arquivos de entrada tenham dados corrompidos, ausentes ou sujos. Tente este experimento:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modifique a função `parse_csv()` para capturar todas as exceções `ValueError` geradas durante a criação do registro e imprimir uma mensagem de aviso para as linhas que não podem ser convertidas.

A mensagem deve incluir o número da linha e informações sobre o motivo da falha. Para testar sua função, tente ler o arquivo `missing.csv` acima. Por exemplo:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}]
>>>
```
