# Ejercicio 2.15: Un ejemplo práctico de enumerate()

Recuerda que el archivo `missing.csv` contiene datos de una cartera de acciones, pero tiene algunas filas con datos faltantes. Usando `enumerate()`, modifica tu programa `pcost.py` de modo que imprima un número de línea junto con el mensaje de advertencia cuando encuentra una entrada incorrecta.

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Fila 4: No se pudo convertir: ['MSFT', '', '51.23']
Fila 7: No se pudo convertir: ['IBM', '', '70.44']
>>>
```

Para hacer esto, necesitarás cambiar algunas partes de tu código.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
     ...
    except ValueError:
        print(f'Fila {rowno}: Fila incorrecta: {row}')
```
