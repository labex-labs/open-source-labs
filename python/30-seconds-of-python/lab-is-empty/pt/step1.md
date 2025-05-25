# Coleção está vazia

Escreva uma função Python chamada `is_empty(val)` que recebe um valor como parâmetro e retorna `True` se o valor for uma sequência ou coleção vazia, e `False` caso contrário.

Para verificar se uma sequência ou coleção está vazia, você pode usar o operador `not` para testar o valor de verdade da sequência ou coleção fornecida. Se a sequência ou coleção estiver vazia, o operador `not` retornará `True`.

Sua função deve ser capaz de lidar com os seguintes tipos de sequências e coleções:

- Listas
- Tuplas
- Conjuntos (Sets)
- Dicionários
- Strings
- Ranges

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
