# Acesso a Atributos

Existe uma forma alternativa de acessar, manipular e gerenciar atributos.

```python
getattr(obj, 'name')          # Same as obj.name
setattr(obj, 'name', value)   # Same as obj.name = value
delattr(obj, 'name')          # Same as del obj.name
hasattr(obj, 'name')          # Tests if attribute exists
```

Exemplo:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Nota: `getattr()` também possui um valor padrão útil *arg\*.

```python
x = getattr(obj, 'x', None)
```
