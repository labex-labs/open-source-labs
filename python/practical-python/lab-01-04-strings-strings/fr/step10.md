# Chaînes brutes

Les chaînes brutes sont des littéraux de chaîne avec un antislash non interprété. Elles sont spécifiées en préfixant la première citation avec une "r" en minuscules.

```python
>>> rs = r'c:\newdata\test' # Chaîne brute (antislash non interprété)
>>> rs
'c:\\newdata\\test'
```

La chaîne est le texte littéral contenu à l'intérieur, exactement comme il a été tapé. Cela est utile dans des situations où l'antislash a une signification spéciale. Exemple : nom de fichier, expressions régulières, etc.
