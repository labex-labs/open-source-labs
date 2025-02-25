# Extraction de segments

L'extraction de segments consiste à extraire une sous-séquence d'une séquence. La syntaxe est `s[start:end]`. `start` et `end` sont les index de la sous-séquence que vous souhaitez.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

- Les index `start` et `end` doivent être des entiers.
- Les extractions de segments _n'incluent pas_ la valeur de fin. C'est comme un intervalle demi-ouvert en mathématiques.
- Si les index sont omis, ils prennent la valeur par défaut du début ou de la fin de la liste.
