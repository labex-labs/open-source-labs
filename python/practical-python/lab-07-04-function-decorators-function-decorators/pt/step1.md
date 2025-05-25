# Exemplo de Logging (Registro)

Considere uma função.

```python
def add(x, y):
    return x + y
```

Agora, considere a função com algum _logging_ (registro) adicionado.

```python
def add(x, y):
    print('Calling add')
    return x + y
```

Agora, uma segunda função também com algum _logging_ (registro).

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```
