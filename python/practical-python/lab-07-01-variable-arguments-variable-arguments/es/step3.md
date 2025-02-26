# Combinando ambos

Una función también puede aceptar cualquier número de argumentos variables de palabras clave y no de palabras clave.

```python
def f(*args, **kwargs):
...
```

Llamada a la función.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Los argumentos se separan en componentes posicionales y de palabras clave

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
  ...
```

Esta función acepta cualquier combinación de argumentos posicionales o de palabras clave. A veces se utiliza cuando se escriben envoltorios o cuando se desea pasar argumentos a otra función.
