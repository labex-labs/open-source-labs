# Dicionários e Módulos

Dentro de um módulo, um dicionário armazena todas as variáveis e funções globais.

```python
# foo.py

x = 42
def bar():
    ...

def spam():
    ...
```

Se você inspecionar `foo.__dict__` ou `globals()`, você verá o dicionário.

```python
{
    'x' : 42,
    'bar' : <function bar>,
    'spam' : <function spam>
}
```
