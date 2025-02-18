# Snakecase String

Écrivez une fonction Python appelée `snake` qui prend une chaîne de caractères comme argument et renvoie la chaîne en snake case. La fonction devrait effectuer les étapes suivantes :

1. Utilisez `re.sub()` pour trouver tous les mots dans la chaîne, `str.lower()` pour les convertir en minuscules.
2. Utilisez `re.sub()` pour remplacer tous les caractères `-` par des espaces.
3. Enfin, utilisez `str.join()` pour combiner tous les mots en utilisant `_` comme séparateur.

Votre fonction devrait être capable de gérer les chaînes contenant un mélange de lettres majuscules et minuscules, d'espaces, de tirets et de underscores (tirets bas).

```python
from re import sub

def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
