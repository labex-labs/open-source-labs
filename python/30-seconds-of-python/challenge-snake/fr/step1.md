# Snakecase String

## Problème

Écrivez une fonction Python appelée `snake` qui prend une chaîne de caractères en argument et renvoie la chaîne au snake case. La fonction devrait effectuer les étapes suivantes :

1. Utilisez `re.sub()` pour correspondre tous les mots dans la chaîne, `str.lower()` pour les mettre en minuscules.
2. Utilisez `re.sub()` pour remplacer tout caractère `-` par des espaces.
3. Enfin, utilisez `str.join()` pour combiner tous les mots en utilisant `_` comme séparateur.

Votre fonction devrait être capable de gérer les chaînes de caractères contenant une combinaison de lettres majuscules et minuscules, d'espaces, d'hyphens et de tirets du bas.

## Exemple

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
