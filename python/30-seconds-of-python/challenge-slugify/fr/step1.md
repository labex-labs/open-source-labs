# Défi de conversion de chaîne de caractères en slug

## Problème

Écrivez une fonction `slugify(s)` qui prend une chaîne de caractères `s` en argument et renvoie un slug. La fonction doit effectuer les opérations suivantes :

1. Convertir la chaîne de caractères en minuscules et supprimer tout espace blanc en début ou en fin de chaîne.
2. Remplacer tous les caractères spéciaux (c'est-à-dire tout caractère qui n'est pas une lettre, un chiffre, un espace blanc, un tiret ou un tiret bas) par une chaîne de caractères vide.
3. Remplacer tous les espaces blancs, tirets et tirets bas par un seul tiret.
4. Supprimer tout tiret en début ou en fin de chaîne.

## Exemple

```python
slugify('Hello World!') # 'hello-world'
slugify('  My Example 123  ') #'my-example-123'
slugify('This is a long sentence with spaces and punctuation!') # 'this-is-a-long-sentence-with-spaces-and-punctuation'
```
