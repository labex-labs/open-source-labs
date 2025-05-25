# Verificar se a Chave Existe no Dicionário

Escreva uma função `key_in_dict(d, key)` que recebe um dicionário `d` e uma chave `key` como argumentos e retorna `True` se a chave existir no dicionário, `False` caso contrário.

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
