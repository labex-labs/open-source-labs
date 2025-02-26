# Lanzando excepciones

En el archivo `cofollow.py`, creaste una corrutina `printer()`. Modifica el código para capturar y reportar excepciones de la siguiente manera:

```python
# cofollow.py
...
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

Ahora, prueba un experimento:

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('It failed'))
ERROR: ValueError('It failed',)
>>> try:
        int('n/a')
    except ValueError as e:
        p.throw(e)

ERROR: ValueError("invalid literal for int() with base 10: 'n/a'",)
>>>
```

Observa cómo el generador en ejecución no se termina por la excepción. Esto simplemente permite que la instrucción `yield` señale un error en lugar de recibir un valor.
