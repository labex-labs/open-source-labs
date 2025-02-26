# Diccionarios y Módulos

Dentro de un módulo, un diccionario contiene todas las variables y funciones globales.

```python
# foo.py

x = 42
def bar():
  ...

def spam():
  ...
```

Si inspeccionas `foo.__dict__` o `globals()`, verás el diccionario.

```python
{
    'x' : 42,
    'bar' : <function bar>,
   'spam' : <function spam>
}
```
