# Instâncias e Classes

Instâncias e classes são ligadas. O atributo `__class__` se refere de volta à classe.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

O dicionário da instância armazena dados exclusivos para cada instância, enquanto o dicionário da classe armazena dados compartilhados coletivamente por _todas_ as instâncias.
