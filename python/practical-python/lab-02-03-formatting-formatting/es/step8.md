# Ejercicio 2.10: Imprimiendo una tabla formateada

Repite el bucle `for` del Ejercicio 2.9, pero cambia la instrucción `print` para formatear las tuplas.

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

También puedes expandir los valores y usar `f-strings`. Por ejemplo:

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

Toma las declaraciones anteriores y agréguelas a tu programa `report.py`. Haz que tu programa tome la salida de la función `make_report()` e imprima una tabla formateada adecuadamente como se muestra.
