# Itération et recherche dans une liste

Utilisez `for` pour itérer sur le contenu de la liste.

```python
for name in names:
    # utilisez name
    # par exemple, print(name)
  ...
```

Cela est similaire à une instruction `foreach` d'autres langages de programmation.

Pour trouver rapidement la position d'un élément, utilisez `index()`.

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

Si l'élément est présent plus d'une fois, `index()` renverra l'index de la première occurrence.

Si l'élément n'est pas trouvé, une exception `ValueError` sera levée.
