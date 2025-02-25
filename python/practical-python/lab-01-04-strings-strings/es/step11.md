# Cadenas f

Una cadena con sustitución de expresión formateada.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

**Nota: Esto requiere Python 3.6 o posterior.** El significado de los códigos de formato se describe más adelante.

En estos ejercicios, experimentarás con operaciones en el tipo de cadena de Python. Debes hacerlo en el prompt interactivo de Python donde puedes ver fácilmente los resultados. Nota importante:

> En los ejercicios donde se supone que debes interactuar con el intérprete, `>>>` es el prompt del intérprete que obtienes cuando Python te pide que escribas una nueva declaración. Algunas declaraciones en el ejercicio abarcan varias líneas: para que estas declaraciones se ejecuten, es posible que tengas que presionar 'enter' varias veces. Solo un recordatorio de que _NO_ escribes el `>>>` cuando trabajas estos ejemplos.

Comienza definiendo una cadena que contenga una serie de símbolos de cotización de acciones como esta:

```python
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```
