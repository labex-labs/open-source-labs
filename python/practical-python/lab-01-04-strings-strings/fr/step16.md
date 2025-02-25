# Exercice 1.17 : f-strings

Parfois, vous voulez créer une chaîne de caractères et intégrer les valeurs de variables à l'intérieur.

Pour ce faire, utilisez une f-string. Par exemple :

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} parts de {name} à ${price:0.2f}'
'100 parts de IBM à $91.10'
>>>
```

Modifiez le programme `mortgage.py` de l'exercice 1.10 pour créer sa sortie à l'aide de f-strings. Essayez de le faire de manière à ce que la sortie soit bien alignée.
