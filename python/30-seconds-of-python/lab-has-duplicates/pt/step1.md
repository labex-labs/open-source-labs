# Verificando Duplicatas em uma Lista

Escreva uma função Python chamada `has_duplicates(lst)` que recebe uma lista como argumento e retorna `True` se a lista contiver alguma duplicata, e `False` caso contrário.

Para resolver este problema, você pode usar as seguintes etapas:

1.  Use a função `set()` para remover duplicatas da lista.
2.  Compare o comprimento da lista original com o comprimento do conjunto (set). Se forem iguais, então não há duplicatas. Se forem diferentes, então há duplicatas.

```python
def has_duplicates(lst):
  return len(lst) != len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
