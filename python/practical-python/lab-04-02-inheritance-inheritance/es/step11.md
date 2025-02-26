# Herencia múltiple

Puedes heredar de múltiples clases especificándolas en la definición de la clase.

```python
class Mother:
...

class Father:
...

class Child(Mother, Father):
...
```

La clase `Child` hereda características de ambos padres. Hay algunos detalles bastante complicados. No lo hagas a menos que sepas lo que estás haciendo. Se dará más información en la siguiente sección, pero no vamos a utilizar la herencia múltiple más adelante en este curso.

Un uso principal de la herencia es escribir código que se pretende extender o personalizar de varias maneras, especialmente en bibliotecas o marcos. Para ilustrar, considera la función `print_report()` en tu programa `report.py`. Debería verse más o menos así:

```python
def print_report(reportdata):
    '''
    Imprime una tabla bien formateada a partir de una lista de tuplas (nombre, acciones, precio, cambio).
    '''
    headers = ('Nombre','Acciones','Precio','Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 +' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

Cuando ejecutes tu programa de informe, deberías obtener una salida como esta:

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Nombre     Acciones      Precio     Cambio
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```
