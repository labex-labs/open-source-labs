# Chave do Valor Mínimo

Escreva uma função `key_of_min(d)` que recebe um dicionário `d` como argumento e retorna a chave do valor mínimo no dicionário.

Para resolver este problema, você pode usar a função `min()` embutida com o parâmetro `key` definido como `dict.get()`. Isso retornará a chave do valor mínimo no dicionário.

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
