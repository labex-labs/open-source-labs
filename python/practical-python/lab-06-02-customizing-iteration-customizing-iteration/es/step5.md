# Ejercicio 6.6: Usar un generador para producir datos

Si se examina el código del Ejercicio 6.5, la primera parte del código está produciendo líneas de datos mientras que las declaraciones al final del bucle `while` están consumiendo los datos. Una característica principal de las funciones generadoras es que se puede mover todo el código de producción de datos a una función reutilizable.

Modifique el código del Ejercicio 6.5 de modo que la lectura del archivo se realice mediante una función generadora `follow(filename)`. Haga que el siguiente código funcione:

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Should see lines of output produced here...
```

Modifique el código del cotizador de valores para que se vea así:

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
