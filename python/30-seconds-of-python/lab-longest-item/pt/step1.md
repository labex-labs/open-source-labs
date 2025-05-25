# Item Mais Longo (Longest Item)

Escreva uma função `longest_item(*args)` que recebe qualquer número de objetos iteráveis ou objetos com uma propriedade de comprimento (length) e retorna o mais longo. A função deve:

- Usar `max()` com `len()` como a `key` para retornar o item com o maior comprimento.
- Se múltiplos itens tiverem o mesmo comprimento, o primeiro será retornado.

```python
def longest_item(*args):
  return max(args, key = len)
```

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```
