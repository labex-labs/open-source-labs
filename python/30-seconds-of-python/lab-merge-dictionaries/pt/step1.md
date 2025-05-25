# Mesclar Dicionários

Escreva uma função `merge_dictionaries(*dicts)` que recebe dois ou mais dicionários como argumentos e retorna um novo dicionário que contém todos os pares chave-valor dos dicionários de entrada.

Sua função deve criar um novo dicionário e iterar sobre os dicionários de entrada, usando `dictionary.update()` para adicionar os pares chave-valor de cada um ao resultado.

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
