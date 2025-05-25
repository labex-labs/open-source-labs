# Exercício 4.9: Melhor saída para impressão de objetos

Modifique o objeto `Stock` que você definiu em `stock.py` para que o método `__repr__()` produza uma saída mais útil. Por exemplo:

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Veja o que acontece quando você lê um portfólio de ações e visualiza a lista resultante após fazer essas alterações. Por exemplo:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... see what the output is ...
>>>
```
