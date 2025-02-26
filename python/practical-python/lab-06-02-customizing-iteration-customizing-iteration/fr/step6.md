# Exercice 6.7 : Surveiller votre portefeuille

Modifiez le programme `follow.py` de sorte qu'il surveille le flux de données boursières et affiche une cotation montrant les informations seulement pour les actions d'un portefeuille. Par exemple :

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Remarque : Pour que cela fonctionne, votre classe `Portfolio` doit supporter l'opérateur `in`. Consultez l'Exercice 6.3 et assurez-vous d'avoir implémenté l'opérateur `__contains__()`.
