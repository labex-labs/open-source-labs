# Atribuição

Muitas operações em Python estão relacionadas à _atribuição_ ou _armazenamento_ de valores.

```python
a = value         # Assignment to a variable
s[n] = value      # Assignment to a list
s.append(value)   # Appending to a list
d['key'] = value  # Adding to a dictionary
```

_Uma advertência: operações de atribuição **nunca fazem uma cópia** do valor que está sendo atribuído._ Todas as atribuições são meramente cópias de referência (ou cópias de ponteiro, se preferir).
