# Agrupar Elementos de Lista

Escreva uma função `group_by(lst, fn)` que recebe uma lista `lst` e uma função `fn` como argumentos e retorna um dicionário onde as chaves são os resultados da aplicação de `fn` aos elementos de `lst` e os valores são listas de elementos de `lst` que produzem a chave correspondente quando `fn` é aplicada a eles.

Por exemplo, se tivermos uma lista de números `[6.1, 4.2, 6.3]` e quisermos agrupá-los pela sua parte inteira, podemos usar a função `floor` do módulo `math` como a função de agrupamento. A saída esperada seria `{4: [4.2], 6: [6.1, 6.3]}`.

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
