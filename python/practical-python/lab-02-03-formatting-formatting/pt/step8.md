# Exercício 2.10: Imprimindo uma tabela formatada

Refaça o loop for no Exercício 2.9, mas altere a instrução print para formatar as tuplas.

```python
>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

Você também pode expandir os valores e usar f-strings. Por exemplo:

```python
>>> for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

Pegue as instruções acima e adicione-as ao seu programa `report.py`. Faça com que seu programa pegue a saída da função `make_report()` e imprima uma tabela bem formatada, conforme mostrado.
