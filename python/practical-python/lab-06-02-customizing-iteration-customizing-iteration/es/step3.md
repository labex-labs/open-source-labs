# Ejercicio 6.4: Un generador simple

Si alguna vez se encuentra deseando personalizar la iteración, siempre debe pensar en funciones generadoras. Son fáciles de escribir: cree una función que realice la lógica de iteración deseada y use `yield` para emitir valores.

Por ejemplo, pruebe este generador que busca en un archivo líneas que contengan una subcadena coincidente:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

Esto es un poco interesante: la idea de que se puede ocultar un montón de procesamiento personalizado en una función y usarlo para alimentar un bucle `for`. El siguiente ejemplo examina un caso más inusual.
