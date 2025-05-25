# Exercício 6.7: Monitorando seu portfólio

Modifique o programa `follow.py` para que ele monitore o fluxo de dados de ações e imprima um ticker mostrando informações apenas para as ações em um portfólio. Por exemplo:

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

Observação: Para que isso funcione, sua classe `Portfolio` deve suportar o operador `in`. Consulte o Exercício 6.3 e certifique-se de implementar o operador `__contains__()`.
