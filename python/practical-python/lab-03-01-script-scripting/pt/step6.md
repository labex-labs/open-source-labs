# Definição de Função

Funções podem ser _definidas_ em qualquer ordem.

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# OR
def bar(x):
    statements

def foo(x):
    bar(x)
```

As funções só devem ser definidas antes de serem realmente _usadas_ (ou chamadas) durante a execução do programa.

```python
foo(3)        # foo must be defined already
```

Estilisticamente, é provavelmente mais comum ver funções definidas de forma _bottom-up_ (de baixo para cima).
