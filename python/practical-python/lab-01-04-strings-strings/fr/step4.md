# Indexation des chaînes de caractères

Les chaînes de caractères fonctionnent comme un tableau pour accéder à des caractères individuels. Vous utilisez un indice entier, commençant à 0. Les indices négatifs spécifient une position relative à la fin de la chaîne.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (fin de la chaîne)
```

Vous pouvez également extraire ou sélectionner des sous-chaînes en spécifiant une plage d'indices avec `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

Le caractère à l'indice de fin n'est pas inclus. Les indices manquants supposent le début ou la fin de la chaîne.
