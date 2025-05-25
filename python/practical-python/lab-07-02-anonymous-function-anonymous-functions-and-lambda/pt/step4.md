# Usando lambda

- lambda é altamente restrito.
- Apenas uma única expressão é permitida.
- Nenhuma declaração como `if`, `while`, etc.
- O uso mais comum é com funções como `sort()`.

Leia alguns dados de portfólio de ações e converta-os em uma lista:

```python
>>> import report
>>> portfolio = list(report.read_portfolio('portfolio.csv'))
>>> for s in portfolio:
        print(s)

Stock('AA', 100, 32.2)
Stock('IBM', 50, 91.1)
Stock('CAT', 150, 83.44)
Stock('MSFT', 200, 51.23)
Stock('GE', 95, 40.37)
Stock('MSFT', 50, 65.1)
Stock('IBM', 100, 70.44)
>>>
```
