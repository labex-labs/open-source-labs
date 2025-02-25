# String to Slug

Écrivez une fonction `slugify(s)` qui prend une chaîne de caractères `s` en argument et renvoie un slug. La fonction doit effectuer les opérations suivantes :

1. Convertir la chaîne en minuscules et supprimer tout espace blanc en début ou en fin de chaîne.
2. Remplacer tous les caractères spéciaux (c'est-à-dire tout caractère qui n'est pas une lettre, un chiffre, un espace blanc, un tiret ou un tiret bas) par une chaîne vide.
3. Remplacer tous les espaces blancs, tirets et tirets bas par un seul tiret.
4. Supprimer tout tiret en début ou en fin de chaîne.

```python
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```python
slugify('Hello World!') # 'hello-world'
```
