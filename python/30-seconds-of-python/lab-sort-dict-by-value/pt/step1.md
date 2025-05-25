# Ordenar Dicionário

Escreva uma função chamada `sort_dict_by_value(d, reverse=False)` que recebe um dicionário `d` e o ordena por seus valores. A função deve retornar um novo dicionário com as mesmas chaves do dicionário original, mas com os valores ordenados em ordem crescente. Se o parâmetro `reverse` for definido como `True`, a função deve ordenar o dicionário em ordem decrescente.

Para resolver este problema, você pode seguir estes passos:

1. Use `dict.items()` para obter uma lista de pares de tuplas de `d`.
2. Ordene a lista usando uma função lambda e `sorted()`.
3. Use `dict()` para converter a lista ordenada de volta em um dicionário.
4. Use o parâmetro `reverse` em `sorted()` para ordenar o dicionário em ordem inversa, com base no segundo argumento.

**⚠️ AVISO:** Os valores do dicionário devem ser do mesmo tipo.

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
