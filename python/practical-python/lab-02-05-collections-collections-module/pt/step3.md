# Exemplo: Mapeamentos Um-Muitos

Problema: Você quer mapear uma chave para múltiplos valores.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

Como no exemplo anterior, a chave `IBM` deve ter duas tuplas diferentes em vez disso.

Solução: Use um `defaultdict`.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

O `defaultdict` garante que toda vez que você acessa uma chave, você obtém um valor padrão.
