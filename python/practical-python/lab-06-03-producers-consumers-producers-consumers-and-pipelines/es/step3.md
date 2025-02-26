# Ejercicio 6.8: Configurar una tubería simple

Veamos en acción la idea de tuberías. Escribe la siguiente función:

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

Esta función es casi exactamente igual que el primer ejemplo de generador del ejercicio anterior, excepto que ya no está abriendo un archivo, sino que simplemente opera sobre una secuencia de líneas que se le pasa como argumento. Ahora, prueba esto:

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... espera a que aparezca la salida...
```

Puede tardar un poco en aparecer la salida, pero eventualmente deberías ver algunas líneas que contengan datos de GOOG.

Nota: Estos ejercicios deben realizarse simultáneamente en dos terminales separadas.
