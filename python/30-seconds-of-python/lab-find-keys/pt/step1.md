# Encontrar Chaves com Valor

Escreva uma função Python chamada `find_keys(dictionary, value)` que recebe um dicionário e um valor como argumentos e retorna uma lista de todas as chaves no dicionário que possuem o valor fornecido. Se não houver chaves com o valor fornecido, a função deve retornar uma lista vazia.

Para resolver este problema, você pode usar o método `dictionary.items()`, que retorna um gerador que produz pares chave-valor do dicionário. Você pode então usar uma compreensão de lista para filtrar as chaves que possuem o valor fornecido.

```python
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```
