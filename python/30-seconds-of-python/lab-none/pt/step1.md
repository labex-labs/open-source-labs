# Testar se cada elemento da lista é falsy

Escreva uma função Python chamada `none(lst, fn = lambda x: x)` que recebe uma lista `lst` e uma função opcional `fn` como argumentos. A função deve retornar `True` se cada elemento na lista for falsy, e `False` caso contrário. Se a função opcional `fn` for fornecida, ela deve ser usada para determinar a truthiness (veracidade) de cada elemento na lista.

Para determinar se um elemento é falsy, você pode usar as mesmas regras da função `bool()` do Python. Em geral, os seguintes valores são considerados falsy:

- `False`
- `None`
- `0` (inteiro)
- `0.0` (float)
- `''` (string vazia)
- `[]` (lista vazia)
- `{}` (dicionário vazio)
- `()` (tupla vazia)
- `set()` (conjunto vazio)

Se a função opcional `fn` for fornecida, ela deve receber um argumento e retornar um valor booleano. A função será chamada para cada elemento na lista, e o valor de retorno será usado para determinar a truthiness do elemento.

```python
def none(lst, fn = lambda x: x):
  return all(not fn(x) for x in lst)
```

```python
none([0, 1, 2, 0], lambda x: x >= 2 ) # False
none([0, 0, 0]) # True
```
