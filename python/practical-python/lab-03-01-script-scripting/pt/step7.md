# Estilo Bottom-up

Funções são tratadas como blocos de construção. Os blocos menores/mais simples vêm primeiro.

```python
# myprogram.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Defined above
    ...

def spam(x):
    ...
    bar(x)          # Defined above
    ...

spam(42)            # Code that uses the functions appears at the end
```

Funções posteriores constroem-se sobre funções anteriores. Novamente, este é apenas um ponto de estilo. A única coisa que importa no programa acima é que a chamada para `spam(42)` venha por último.
