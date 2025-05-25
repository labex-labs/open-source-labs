# Mapear Lista para Dicionário

Escreva uma função Python chamada `map_dictionary(itr, fn)` que recebe dois parâmetros:

- `itr`: uma lista de valores
- `fn`: uma função que recebe um valor como entrada e retorna um valor como saída

A função deve retornar um dicionário onde os pares chave-valor consistem no valor original como chave e o resultado da função como valor.

Para resolver este problema, siga estes passos:

1. Use `map()` para aplicar `fn` a cada valor da lista.
2. Use `zip()` para emparelhar os valores originais com os valores produzidos por `fn`.
3. Use `dict()` para retornar um dicionário apropriado.

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
