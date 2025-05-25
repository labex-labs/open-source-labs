# Verificar se Duas Listas Possuem o Mesmo Conteúdo

Escreva uma função `have_same_contents(a, b)` que recebe duas listas como argumentos e retorna `True` se elas possuem o mesmo conteúdo, e `False` caso contrário. A função deve verificar se as duas listas contêm os mesmos elementos, independentemente da sua ordem.

Para resolver este problema, você pode seguir estes passos:

1.  Use `set()` na combinação de ambas as listas para encontrar os valores únicos.
2.  Itere sobre eles com um loop `for` comparando o `count()` de cada valor único em cada lista.
3.  Retorne `False` se as contagens não corresponderem para nenhum elemento, e `True` caso contrário.

```python
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v) != b.count(v):
      return False
  return True
```

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
