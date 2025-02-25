# Ejercicio 1.26: Preliminares de archivos

Primero, intenta leer todo el archivo de una vez como una gran cadena:

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

En el ejemplo anterior, hay que notar que Python tiene dos modos de salida. En el primer modo donde escribes `data` en el prompt, Python te muestra la representación de cadena sin procesar incluyendo comillas y códigos de escape. Cuando escribes `print(data)`, obtienes la salida formateada real de la cadena.

Aunque leer un archivo de una vez es simple, a menudo no es la forma más adecuada de hacerlo, especialmente si el archivo resulta ser enorme o si contiene líneas de texto que quieres manejar una a la vez.

Para leer un archivo línea por línea, utiliza un bucle `for` de la siguiente manera:

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

Cuando utilizas este código como se muestra, se leen las líneas hasta que se alcanza el final del archivo, momento en el que el bucle se detiene.

En ciertas ocasiones, es posible que desees leer manualmente o omitir una _única_ línea de texto (por ejemplo, quizás desees omitir la primera línea de encabezados de columna).

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` devuelve la siguiente línea de texto del archivo. Si lo llamaras repetidamente, obtendrías líneas sucesivas. Sin embargo, para que lo sepas, el bucle `for` ya utiliza `next()` para obtener sus datos. Por lo tanto, normalmente no lo llamarías directamente a menos que estés intentando omitir o leer explícitamente una sola línea como se muestra.

Una vez que estás leyendo las líneas de un archivo, puedes comenzar a realizar más procesamiento, como dividir. Por ejemplo, prueba esto:

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name','shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_Nota: En estos ejemplos, se está llamando explícitamente a `f.close()` porque no se está utilizando la declaración `with`._
