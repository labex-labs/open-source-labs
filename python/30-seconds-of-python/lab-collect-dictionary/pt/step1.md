# Inverter um Dicionário

Escreva uma função `invert_dictionary(obj)` que recebe um dicionário `obj` como entrada e retorna um novo dicionário com as chaves e os valores invertidos. O dicionário de entrada terá valores hashable não únicos. Se duas ou mais chaves tiverem o mesmo valor, a função deve anexar as chaves a uma lista no dicionário de saída.

Para resolver este problema, você pode seguir estes passos:

1. Crie um `collections.defaultdict` com `list` como o valor padrão para cada chave.
2. Use `dictionary.items()` em combinação com um loop para mapear os valores do dicionário para chaves usando `dict.append()`.
3. Use `dict()` para converter o `collections.defaultdict` em um dicionário regular.

Assinatura da função: `def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
