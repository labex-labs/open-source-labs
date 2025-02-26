# Definición de funciones

Las funciones se pueden _definir_ en cualquier orden.

```python
def foo(x):
    bar(x)

def bar(x):
    instrucciones

# O
def bar(x):
    instrucciones

def foo(x):
    bar(x)
```

Las funciones solo deben definirse antes de ser _utilizadas_ (o llamadas) durante la ejecución del programa.

```python
foo(3)        # foo debe estar ya definido
```

En términos de estilo, probablemente sea más común ver funciones definidas de manera _de abajo hacia arriba_.
