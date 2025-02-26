# Programmation par contrat

Connue également sous le nom de Conception par Contrat, l'utilisation extensive d'assertions est une approche pour concevoir des logiciels. Elle stipule que les concepteurs de logiciels devraient définir des spécifications d'interface précises pour les composants du logiciel.

Par exemple, vous pourriez placer des assertions sur toutes les entrées d'une fonction.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

Vérifier les entrées permettra immédiatement de détecter les appelants qui n'utilisent pas les arguments appropriés.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
