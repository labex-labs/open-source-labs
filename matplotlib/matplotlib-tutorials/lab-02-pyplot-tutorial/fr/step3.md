# Tracer plusieurs lignes

Nous pouvons également tracer plusieurs lignes avec différents styles dans un appel de fonction en utilisant des tableaux. Traçons trois lignes : une ligne rouge pointillée, des carrés bleus et des triangles verts :

```python
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

Explication :

- Nous utilisons le module `numpy` pour créer un tableau `t` avec des valeurs d'un temps régulièrement échantillonnées.
- La fonction `plot` est appelée avec trois paires de valeurs `x` et `y`, suivies des chaînes de formatage `'r--'` (ligne rouge pointillée), `'bs'` (carrés bleus) et `'g^'` (triangles verts).
