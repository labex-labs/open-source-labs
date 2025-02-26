# Utilisation de lambda

- lambda est fortement restreint.
- Seule une seule expression est autorisée.
- Aucune instruction comme `if`, `while`, etc.
- L'utilisation la plus courante est avec des fonctions comme `sort()`.

Lire des données de portefeuille d'actions et les convertir en une liste :

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
