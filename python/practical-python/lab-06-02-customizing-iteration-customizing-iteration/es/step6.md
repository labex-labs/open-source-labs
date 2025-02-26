# Ejercicio 6.7: Vigilar su cartera

Modifique el programa `follow.py` de modo que observe el flujo de datos de las acciones y imprima un cotizador que muestre información solo para aquellas acciones que se encuentran en una cartera. Por ejemplo:

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

Nota: Para que esto funcione, su clase `Portfolio` debe admitir el operador `in`. Consulte el Ejercicio 6.3 y asegúrese de implementar el operador `__contains__()`.
