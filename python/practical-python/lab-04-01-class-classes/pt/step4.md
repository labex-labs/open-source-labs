# Dados da Instância (Instance Data)

Cada instância tem seus próprios dados locais.

```python
>>> a.x
2
>>> b.x
10
```

Esses dados são inicializados pelo `__init__()`.

```python
class Player:
    def __init__(self, x, y):
        # Qualquer valor armazenado em `self` é dado da instância
        self.x = x
        self.y = y
        self.health = 100
```

Não há restrições sobre o número total ou o tipo de atributos armazenados.
