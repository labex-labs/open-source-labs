# Chaîne de caractères en kebab case

Écrivez une fonction Python appelée `to_kebab_case(s)` qui prend une chaîne de caractères `s` en entrée et renvoie la version en kebab case de la chaîne. La fonction doit effectuer les étapes suivantes :

1. Remplacez tout `-` ou `_` par un espace, en utilisant l'expression régulière `r"(_|-)+"`.
2. Sélectionnez tous les mots dans la chaîne, `str.lower()` pour les mettre en minuscules.
3. Combinez tous les mots en utilisant `-` comme séparateur.

```python
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```python
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```
