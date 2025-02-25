# Formatage de chaînes de caractères

Une manière de formater des chaînes de caractères en Python 3.6+ est d'utiliser les `f-strings`.

```python
>>> nom = 'IBM'
>>> actions = 100
>>> prix = 91.1
>>> f'{nom:>10s} {actions:>10d} {prix:>10.2f}'
'       IBM        100      91,10'
>>>
```

La partie `{expression:format}` est remplacée.

Elle est couramment utilisée avec `print`.

```python
print(f'{nom:>10s} {actions:>10d} {prix:>10.2f}')
```
