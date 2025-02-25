# Chaîne de caractères en kebab case

## Problème

Écrivez une fonction Python appelée `to_kebab_case(s)` qui prend une chaîne de caractères `s` en entrée et renvoie la version en kebab case de la chaîne. La fonction doit effectuer les étapes suivantes :

1. Remplacez tout `-` ou `_` par un espace, en utilisant l'expression régulière `r"(_|-)+"`.
2. Sélectionnez tous les mots dans la chaîne, puis utilisez `str.lower()` pour les mettre en minuscules.
3. Combinez tous les mots en utilisant `-` comme séparateur.

## Exemple

```python
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```
