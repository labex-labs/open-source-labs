# Exercice 2.8 : Comment formater des nombres

Un problème courant lors de l'affichage de nombres est de spécifier le nombre de décimales. Une manière de résoudre ce problème est d'utiliser les `f-strings`. Essayez ces exemples :

```python
>>> valeur = 42863.1
>>> print(valeur)
42863.1
>>> print(f'{valeur:0.4f}')
42863.1000
>>> print(f'{valeur:>16.2f}')
        42863.10
>>> print(f'{valeur:<16.2f}')
42863.10
>>> print(f'{valeur:*>16,.2f}')
*******42,863.10
>>>
```

La documentation complète sur les codes de formatage utilisés dans les `f-strings` peut être trouvée [ici](https://docs.python.org/3/library/string.html#format-specification-mini-language). Le formatage est également parfois effectué à l'aide de l'opérateur `%` des chaînes de caractères.

```python
>>> print('%0.4f' % valeur)
42863.1000
>>> print('%16.2f' % valeur)
        42863.10
>>>
```

La documentation sur les différents codes utilisés avec `%` peut être trouvée [ici](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Bien que cela soit couramment utilisé avec `print`, le formatage de chaînes n'est pas lié à l'affichage. Si vous voulez enregistrer une chaîne de caractères formatée. Assignez simplement la chaîne à une variable.

```python
>>> f = '%0.4f' % valeur
>>> f
'42863.1000'
>>>
```
